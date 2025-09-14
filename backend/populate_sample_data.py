#!/usr/bin/env python3
"""
Sample Data Population Script for Xeno Shopify Analytics
This script populates the database with realistic sample data for demonstration
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.tenant import Tenant
from app.models.user import User
from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from passlib.context import CryptContext
import random
from datetime import datetime, timedelta
from decimal import Decimal

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_sample_data():
    db: Session = SessionLocal()
    
    try:
        # Create sample tenants (Shopify stores)
        tenants_data = [
            {
                "name": "Fashion Forward Store",
                "shopify_store_url": "fashion-forward-demo.myshopify.com",
                "shopify_access_token": "sample_token_1"
            },
            {
                "name": "Tech Gadgets Hub",
                "shopify_store_url": "tech-gadgets-demo.myshopify.com", 
                "shopify_access_token": "sample_token_2"
            },
            {
                "name": "Home & Garden Paradise",
                "shopify_store_url": "home-garden-demo.myshopify.com",
                "shopify_access_token": "sample_token_3"
            }
        ]
        
        created_tenants = []
        for tenant_data in tenants_data:
            existing_tenant = db.query(Tenant).filter(Tenant.shopify_store_url == tenant_data["shopify_store_url"]).first()
            if not existing_tenant:
                tenant = Tenant(**tenant_data)
                db.add(tenant)
                db.flush()
                created_tenants.append(tenant)
                print(f"✅ Created tenant: {tenant.name}")
            else:
                created_tenants.append(existing_tenant)
                print(f"⚠️  Tenant already exists: {existing_tenant.name}")
        
        # Create sample users for each tenant
        users_data = [
            {"email": "admin@fashionforward.com", "password": "admin123", "full_name": "Fashion Admin"},
            {"email": "manager@techgadgets.com", "password": "manager123", "full_name": "Tech Manager"},
            {"email": "owner@homegarden.com", "password": "owner123", "full_name": "Garden Owner"}
        ]
        
        created_users = []
        for i, user_data in enumerate(users_data):
            existing_user = db.query(User).filter(User.email == user_data["email"]).first()
            if not existing_user:
                user = User(
                    email=user_data["email"],
                    hashed_password=get_password_hash(user_data["password"]),
                    tenant_id=created_tenants[i].id
                )
                db.add(user)
                db.flush()
                created_users.append(user)
                print(f"✅ Created user: {user.email}")
            else:
                created_users.append(existing_user)
                print(f"⚠️  User already exists: {existing_user.email}")
        
        # Create sample products for each tenant
        products_data = [
            # Fashion Forward Store Products
            [
                {"title": "Premium Cotton T-Shirt", "vendor": "Fashion Co", "product_type": "Apparel"},
                {"title": "Designer Jeans", "vendor": "Denim Masters", "product_type": "Apparel"},
                {"title": "Leather Handbag", "vendor": "Luxury Goods", "product_type": "Accessories"},
                {"title": "Summer Dress", "vendor": "Style Studio", "product_type": "Apparel"},
                {"title": "Sneakers", "vendor": "Comfort Shoes", "product_type": "Footwear"}
            ],
            # Tech Gadgets Hub Products
            [
                {"title": "Wireless Earbuds", "vendor": "Audio Tech", "product_type": "Electronics"},
                {"title": "Smartphone Case", "vendor": "Mobile Accessories", "product_type": "Electronics"},
                {"title": "Portable Charger", "vendor": "PowerUp", "product_type": "Electronics"},
                {"title": "Bluetooth Speaker", "vendor": "Sound Wave", "product_type": "Electronics"},
                {"title": "Smart Watch", "vendor": "Wearable Tech", "product_type": "Electronics"}
            ],
            # Home & Garden Paradise Products
            [
                {"title": "Indoor Plant Pot", "vendor": "Garden Essentials", "product_type": "Home Decor"},
                {"title": "Kitchen Knife Set", "vendor": "Chef's Choice", "product_type": "Kitchen"},
                {"title": "Throw Pillow", "vendor": "Comfort Home", "product_type": "Home Decor"},
                {"title": "Garden Hose", "vendor": "Outdoor Tools", "product_type": "Garden"},
                {"title": "Coffee Maker", "vendor": "Morning Brew", "product_type": "Kitchen"}
            ]
        ]
        
        created_products = []
        for tenant_idx, tenant_products in enumerate(products_data):
            tenant_product_list = []
            for product_data in tenant_products:
                product = Product(
                    shopify_product_id=str(random.randint(100000, 999999)),
                    title=product_data["title"],
                    vendor=product_data["vendor"],
                    product_type=product_data["product_type"],
                    tenant_id=created_tenants[tenant_idx].id
                )
                db.add(product)
                db.flush()
                tenant_product_list.append(product)
            created_products.append(tenant_product_list)
            print(f"✅ Created {len(tenant_products)} products for {created_tenants[tenant_idx].name}")
        
        # Create sample customers for each tenant
        customers_data = [
            # Fashion Forward Store Customers
            [
                {"first_name": "Emma", "last_name": "Johnson", "email": "emma.johnson@email.com"},
                {"first_name": "Michael", "last_name": "Brown", "email": "michael.brown@email.com"},
                {"first_name": "Sarah", "last_name": "Davis", "email": "sarah.davis@email.com"},
                {"first_name": "James", "last_name": "Wilson", "email": "james.wilson@email.com"},
                {"first_name": "Lisa", "last_name": "Anderson", "email": "lisa.anderson@email.com"}
            ],
            # Tech Gadgets Hub Customers
            [
                {"first_name": "David", "last_name": "Miller", "email": "david.miller@email.com"},
                {"first_name": "Jennifer", "last_name": "Garcia", "email": "jennifer.garcia@email.com"},
                {"first_name": "Robert", "last_name": "Martinez", "email": "robert.martinez@email.com"},
                {"first_name": "Amanda", "last_name": "Taylor", "email": "amanda.taylor@email.com"},
                {"first_name": "Christopher", "last_name": "Thomas", "email": "christopher.thomas@email.com"}
            ],
            # Home & Garden Paradise Customers
            [
                {"first_name": "Michelle", "last_name": "White", "email": "michelle.white@email.com"},
                {"first_name": "Kevin", "last_name": "Lee", "email": "kevin.lee@email.com"},
                {"first_name": "Rachel", "last_name": "Harris", "email": "rachel.harris@email.com"},
                {"first_name": "Daniel", "last_name": "Clark", "email": "daniel.clark@email.com"},
                {"first_name": "Ashley", "last_name": "Lewis", "email": "ashley.lewis@email.com"}
            ]
        ]
        
        created_customers = []
        for tenant_idx, tenant_customers in enumerate(customers_data):
            tenant_customer_list = []
            for customer_data in tenant_customers:
                customer = Customer(
                    shopify_customer_id=str(random.randint(100000, 999999)),
                    first_name=customer_data["first_name"],
                    last_name=customer_data["last_name"],
                    email=customer_data["email"],
                    total_spent=0.0,
                    created_at=datetime.utcnow(),
                    tenant_id=created_tenants[tenant_idx].id
                )
                db.add(customer)
                db.flush()
                tenant_customer_list.append(customer)
            created_customers.append(tenant_customer_list)
            print(f"✅ Created {len(tenant_customers)} customers for {created_tenants[tenant_idx].name}")
        
        # Create sample orders for each tenant
        for tenant_idx in range(len(created_tenants)):
            tenant = created_tenants[tenant_idx]
            products = created_products[tenant_idx]
            customers = created_customers[tenant_idx]
            
            # Create 20-30 orders per tenant over the last 90 days
            num_orders = random.randint(20, 30)
            for _ in range(num_orders):
                # Random date within last 90 days
                days_ago = random.randint(1, 90)
                order_date = datetime.utcnow() - timedelta(days=days_ago)
                
                # Random customer and calculate total
                customer = random.choice(customers)
                total_price = round(random.uniform(25.0, 500.0), 2)
                
                order = Order(
                    shopify_order_id=str(random.randint(1000000, 9999999)),
                    total_price=total_price,
                    currency="USD",
                    created_at=order_date,
                    tenant_id=tenant.id
                )
                db.add(order)
            
            print(f"✅ Created {num_orders} orders for {tenant.name}")
        
        db.commit()
        print("\n🎉 Sample data population completed successfully!")
        print("\n📊 Summary:")
        print(f"   • {len(created_tenants)} Tenants (Shopify Stores)")
        print(f"   • {len(created_users)} Users")
        print(f"   • {sum(len(products) for products in created_products)} Products")
        print(f"   • {sum(len(customers) for customers in created_customers)} Customers")
        print(f"   • ~75 Orders across all tenants")
        
        print("\n🔐 Test Login Credentials:")
        for user in created_users:
            tenant_name = next(t.name for t in created_tenants if t.id == user.tenant_id)
            password = "admin123" if "admin" in user.email else "manager123" if "manager" in user.email else "owner123"
            print(f"   • {user.email} | Password: {password} | Store: {tenant_name}")
            
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Starting sample data population...")
    create_sample_data()
