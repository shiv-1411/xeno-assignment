#!/usr/bin/env python3
"""
Real Shopify Store Configuration Script
Run this after you get your real Shopify development store and access token
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.tenant import Tenant
from app.models.user import User
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def update_real_shopify_config():
    """
    Update database with real Shopify store configuration
    
    INSTRUCTIONS:
    1. Create your Shopify Partner account at partners.shopify.com
    2. Create a development store (e.g., 'your-store-name.myshopify.com')  
    3. Create a custom app with permissions: read_customers, read_orders, read_products
    4. Install the app and copy the access token
    5. Update the variables below with your real values
    6. Run this script: python configure_real_shopify.py
    """
    
    # ⚠️ REPLACE THESE WITH YOUR REAL SHOPIFY STORE DETAILS ⚠️
    REAL_STORE_URL = "your-store-name.myshopify.com"  # Replace with your real store URL
    REAL_ACCESS_TOKEN = "shpat_xxxxx"  # Replace with your real access token
    STORE_NAME = "Your Real Store Name"  # Replace with your store name
    
    if REAL_STORE_URL == "your-store-name.myshopify.com" or REAL_ACCESS_TOKEN == "shpat_xxxxx":
        print("🚨 ERROR: Please update the configuration with your real Shopify store details!")
        print("📝 Edit this file and replace REAL_STORE_URL and REAL_ACCESS_TOKEN")
        print("🔗 Follow the setup guide in SHOPIFY_SETUP.md")
        return False
    
    db: Session = SessionLocal()
    
    try:
        print("🔄 Updating database with real Shopify configuration...")
        
        # Clear existing mock tenants
        db.query(Tenant).delete()
        db.query(User).delete()
        
        # Create real tenant with your Shopify store
        real_tenant = Tenant(
            name=STORE_NAME,
            shopify_store_url=REAL_STORE_URL,
            shopify_access_token=REAL_ACCESS_TOKEN
        )
        db.add(real_tenant)
        db.commit()
        db.refresh(real_tenant)
        
        # Create a user for this tenant
        real_user = User(
            email="admin@yourstore.com",
            hashed_password=get_password_hash("password123"),
            first_name="Store",
            last_name="Admin", 
            tenant_id=real_tenant.id
        )
        db.add(real_user)
        db.commit()
        
        print("✅ Successfully configured real Shopify store!")
        print(f"📍 Store URL: {REAL_STORE_URL}")
        print(f"👤 Login Email: admin@yourstore.com") 
        print(f"🔑 Login Password: password123")
        print(f"🆔 Tenant ID: {real_tenant.id}")
        
        print("\n🚀 Next Steps:")
        print("1. Add products to your Shopify store admin")
        print("2. Create some customers and test orders") 
        print("3. Test the ingestion endpoints at http://localhost:8000/docs")
        print("4. Run: POST /api/v1/ingest/shopify/test-connection")
        print("5. Run: POST /api/v1/ingest/shopify/products")
        print("6. Run: POST /api/v1/ingest/shopify/customers") 
        print("7. Run: POST /api/v1/ingest/shopify/orders")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = update_real_shopify_config()
    if success:
        print("\n🎉 Ready for real Shopify API integration!")
    else:
        print("\n💡 Please follow the setup instructions in SHOPIFY_SETUP.md")