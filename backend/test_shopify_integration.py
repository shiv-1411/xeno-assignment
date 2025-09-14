#!/usr/bin/env python3
"""
Test Real Shopify API Integration
Run this to test your real Shopify API connection and data ingestion
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.tenant import Tenant
from app.services.ingestion_service import IngestionService

def test_shopify_integration():
    """Test real Shopify API integration"""
    
    db: Session = SessionLocal()
    
    try:
        # Get the first tenant (should be your real store)
        tenant = db.query(Tenant).first()
        
        if not tenant:
            print("❌ No tenant found! Run configure_real_shopify.py first")
            return False
            
        if tenant.shopify_access_token.startswith("sample_token"):
            print("❌ Still using mock data! Update with real Shopify credentials")
            print("📝 Edit configure_real_shopify.py and run it")
            return False
            
        print(f"🔍 Testing Shopify integration for: {tenant.name}")
        print(f"📍 Store URL: {tenant.shopify_store_url}")
        
        # Initialize ingestion service
        ingestion_service = IngestionService(db, tenant)
        
        # Test connection
        print("\n1️⃣ Testing Shopify API connection...")
        connection_result = ingestion_service.test_connection()
        
        if connection_result["status"] == "success":
            print("✅ Connection successful!")
            print(f"   Shop Name: {connection_result.get('shop_name')}")
            print(f"   Domain: {connection_result.get('shop_domain')}")
            print(f"   Plan: {connection_result.get('plan')}")
        else:
            print(f"❌ Connection failed: {connection_result.get('message')}")
            return False
            
        # Test data ingestion
        print("\n2️⃣ Testing product ingestion...")
        products_result = ingestion_service.ingest_products()
        print(f"   Status: {products_result['status']}")
        if products_result['status'] == 'success':
            print(f"   Created: {products_result.get('created', 0)} products")
            print(f"   Updated: {products_result.get('updated', 0)} products")
        else:
            print(f"   Error: {products_result.get('message')}")
            
        print("\n3️⃣ Testing customer ingestion...")
        customers_result = ingestion_service.ingest_customers()
        print(f"   Status: {customers_result['status']}")
        if customers_result['status'] == 'success':
            print(f"   Created: {customers_result.get('created', 0)} customers")
            print(f"   Updated: {customers_result.get('updated', 0)} customers")
        else:
            print(f"   Error: {customers_result.get('message')}")
            
        print("\n4️⃣ Testing order ingestion...")
        orders_result = ingestion_service.ingest_orders()
        print(f"   Status: {orders_result['status']}")
        if orders_result['status'] == 'success':
            print(f"   Created: {orders_result.get('created', 0)} orders")
            print(f"   Updated: {orders_result.get('updated', 0)} orders")
        else:
            print(f"   Error: {orders_result.get('message')}")
            
        print("\n🎉 Shopify integration test complete!")
        print("💡 Check your dashboard at http://localhost:3000 to see the real data")
        
        return True
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False
    finally:
        db.close()

def manual_api_test():
    """Manual test of Shopify API endpoints"""
    
    print("\n🔧 Manual API Test Instructions:")
    print("1. Start your backend: cd backend && python run.py")
    print("2. Go to: http://localhost:8000/docs")
    print("3. Login with your credentials")
    print("4. Test these endpoints:")
    print("   - GET /api/v1/ingest/shopify/test-connection")
    print("   - POST /api/v1/ingest/shopify/products") 
    print("   - POST /api/v1/ingest/shopify/customers")
    print("   - POST /api/v1/ingest/shopify/orders")
    print("5. Check dashboard for real data!")

if __name__ == "__main__":
    print("🧪 Testing Real Shopify API Integration\n")
    
    success = test_shopify_integration()
    
    if not success:
        manual_api_test()
    
    print("\n📚 Helpful Resources:")
    print("• Shopify Partner Dashboard: https://partners.shopify.com")
    print("• API Documentation: https://shopify.dev/docs/admin-api/rest/reference")
    print("• Your setup guide: SHOPIFY_SETUP.md")