#!/usr/bin/env python3
"""
Deployment Setup Script for Xeno Shopify Analytics
This script sets up the database and populates it with mock data for production deployment
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.tenant import Tenant
from app.models.user import User
from app.services.ingestion_service import IngestionService
from passlib.context import CryptContext
from app.core.config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def setup_deployment():
    """Setup database and populate with mock data for deployment"""
    from app.db.session import ensure_schema_exists
    
    # Ensure schema exists first
    ensure_schema_exists()
    
    print("🚀 Setting up Xeno Shopify Analytics for deployment...")
    print(f"📊 Mock Mode: {'Enabled' if not settings.USE_SHOPIFY_API else 'Disabled'}")
    print(f"🗄️ Database Schema: {settings.DATABASE_SCHEMA}")
    
    db: Session = SessionLocal()
    
    try:
        # Check if tenant already exists
        existing_tenant = db.query(Tenant).first()
        
        if not existing_tenant:
            print("📝 Creating demo tenant...")
            
            # Create demo tenant
            demo_tenant = Tenant(
                name="Xeno Demo Store",
                shopify_store_url="xeno-demo-store.myshopify.com",
                shopify_access_token="demo_token_mock_mode"
            )
            db.add(demo_tenant)
            db.commit()
            db.refresh(demo_tenant)
            
            # Create demo user
            demo_user = User(
                email="demo@xeno.com",
                hashed_password=get_password_hash("demo123"),
                first_name="Demo",
                last_name="User",
                tenant_id=demo_tenant.id
            )
            db.add(demo_user)
            db.commit()
            
            print("✅ Demo tenant and user created")
            print(f"📧 Login Email: demo@xeno.com")
            print(f"🔑 Password: demo123")
            
        else:
            demo_tenant = existing_tenant
            print("✅ Existing tenant found")
        
        # Populate with mock data using ingestion service
        if not settings.USE_SHOPIFY_API:
            print("📦 Populating with mock Shopify data...")
            
            ingestion_service = IngestionService(db, demo_tenant)
            
            # Test connection first
            connection_result = ingestion_service.test_connection()
            print(f"🔗 Connection test: {connection_result['status']} ({connection_result.get('mode', 'unknown')} mode)")
            
            # Ingest mock data
            products_result = ingestion_service.ingest_products()
            customers_result = ingestion_service.ingest_customers()
            orders_result = ingestion_service.ingest_orders()
            
            print(f"✅ Products: {products_result.get('created', 0)} created")
            print(f"✅ Customers: {customers_result.get('created', 0)} created")  
            print(f"✅ Orders: {orders_result.get('created', 0)} created")
            
        print("\n🎉 Deployment setup complete!")
        print("\n📊 Demo Credentials:")
        print("   Email: demo@xeno.com")
        print("   Password: demo123")
        print(f"\n🔧 API Mode: {'Mock (Development)' if not settings.USE_SHOPIFY_API else 'Live (Production)'}")
        print("\n🚀 Your application is ready for production!")
        
        return True
        
    except Exception as e:
        print(f"❌ Setup error: {e}")
        db.rollback()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = setup_deployment()
    if success:
        print("\n✅ Ready to deploy!")
    else:
        print("\n❌ Setup failed - check logs above")