"""
Shopify API Mock Fixtures
Realistic JSON responses matching actual Shopify Admin REST API format
"""

from datetime import datetime, timedelta
import random

class ShopifyMockFixtures:
    """Mock data that matches real Shopify API response formats"""
    
    @staticmethod
    def get_shop_response():
        """Mock /admin/api/2023-10/shop.json response"""
        return {
            "shop": {
                "id": 123456789,
                "name": "Xeno Demo Store",
                "email": "admin@xenodemostore.com",
                "domain": "xeno-demo-store.myshopify.com",
                "province": "California",
                "country": "United States",
                "address1": "123 Commerce Street",
                "zip": "94102",
                "city": "San Francisco",
                "phone": "+1 555-123-4567",
                "created_at": "2023-01-15T10:00:00-05:00",
                "updated_at": "2024-12-01T15:30:00-05:00",
                "currency": "USD",
                "customer_email": "customers@xenodemostore.com",
                "timezone": "(GMT-08:00) America/Los_Angeles",
                "plan_name": "Basic Shopify",
                "plan_display_name": "Basic",
                "shop_owner": "Demo Store Owner",
                "money_format": "${{amount}}",
                "money_with_currency_format": "${{amount}} USD",
                "weight_unit": "lb",
                "province_code": "CA",
                "taxes_included": False,
                "auto_configure_tax_inclusivity": None,
                "county_taxes": True,
                "checkout_api_supported": True,
                "multi_location_enabled": True,
                "setup_required": False,
                "pre_launch_enabled": False,
                "enabled_presentment_currencies": ["USD"]
            }
        }
    
    @staticmethod
    def get_products_response():
        """Mock /admin/api/2023-10/products.json response"""
        base_date = datetime.now() - timedelta(days=30)
        
        products = []
        product_templates = [
            {"title": "Premium Wireless Earbuds", "vendor": "TechSound", "product_type": "Electronics", "price": "89.99"},
            {"title": "Organic Cotton T-Shirt", "vendor": "EcoWear", "product_type": "Apparel", "price": "29.99"},
            {"title": "Smart Fitness Tracker", "vendor": "FitTech", "product_type": "Electronics", "price": "149.99"},
            {"title": "Ceramic Coffee Mug", "vendor": "HomeStyle", "product_type": "Home & Kitchen", "price": "19.99"},
            {"title": "Yoga Mat Pro", "vendor": "ZenFit", "product_type": "Sports", "price": "49.99"},
            {"title": "Bluetooth Speaker", "vendor": "SoundWave", "product_type": "Electronics", "price": "79.99"},
            {"title": "Leather Wallet", "vendor": "CraftLeather", "product_type": "Accessories", "price": "39.99"},
            {"title": "Stainless Steel Water Bottle", "vendor": "HydroLife", "product_type": "Sports", "price": "24.99"},
            {"title": "Desk Organizer", "vendor": "OfficeMax", "product_type": "Office", "price": "34.99"},
            {"title": "Phone Case - Clear", "vendor": "ProtectTech", "product_type": "Electronics", "price": "14.99"},
        ]
        
        for i, template in enumerate(product_templates, 1):
            created_date = base_date + timedelta(days=random.randint(0, 25))
            products.append({
                "id": 1000000000000 + i,
                "title": template["title"],
                "body_html": f"<p>Premium quality {template['title'].lower()} with excellent features and design.</p>",
                "vendor": template["vendor"],
                "product_type": template["product_type"],
                "created_at": created_date.isoformat() + "Z",
                "handle": template["title"].lower().replace(" ", "-"),
                "updated_at": (created_date + timedelta(days=random.randint(1, 5))).isoformat() + "Z",
                "published_at": created_date.isoformat() + "Z",
                "template_suffix": None,
                "status": "active",
                "published_scope": "web",
                "tags": f"{template['product_type']}, Premium, Popular",
                "admin_graphql_api_id": f"gid://shopify/Product/{1000000000000 + i}",
                "variants": [{
                    "id": 2000000000000 + i,
                    "product_id": 1000000000000 + i,
                    "title": "Default Title",
                    "price": template["price"],
                    "sku": f"SKU-{1000 + i}",
                    "position": 1,
                    "inventory_policy": "deny",
                    "compare_at_price": None,
                    "fulfillment_service": "manual",
                    "inventory_management": "shopify",
                    "option1": "Default Title",
                    "option2": None,
                    "option3": None,
                    "created_at": created_date.isoformat() + "Z",
                    "updated_at": created_date.isoformat() + "Z",
                    "taxable": True,
                    "barcode": None,
                    "grams": random.randint(100, 1000),
                    "image_id": None,
                    "weight": round(random.uniform(0.1, 2.0), 2),
                    "weight_unit": "lb",
                    "inventory_item_id": 3000000000000 + i,
                    "inventory_quantity": random.randint(5, 100),
                    "old_inventory_quantity": random.randint(5, 100),
                    "requires_shipping": True,
                    "admin_graphql_api_id": f"gid://shopify/ProductVariant/{2000000000000 + i}"
                }],
                "options": [{
                    "id": 4000000000000 + i,
                    "product_id": 1000000000000 + i,
                    "name": "Title",
                    "position": 1,
                    "values": ["Default Title"]
                }],
                "images": [],
                "image": None
            })
        
        return {"products": products}
    
    @staticmethod
    def get_customers_response():
        """Mock /admin/api/2023-10/customers.json response"""
        base_date = datetime.now() - timedelta(days=60)
        
        customer_templates = [
            {"first_name": "Emma", "last_name": "Johnson", "email": "emma.johnson@email.com", "spent": 816.84},
            {"first_name": "Michael", "last_name": "Brown", "email": "michael.brown@email.com", "spent": 454.45},
            {"first_name": "Sarah", "last_name": "Davis", "email": "sarah.davis@email.com", "spent": 1205.32},
            {"first_name": "James", "last_name": "Wilson", "email": "james.wilson@email.com", "spent": 892.17},
            {"first_name": "Lisa", "last_name": "Anderson", "email": "lisa.anderson@email.com", "spent": 673.98},
            {"first_name": "David", "last_name": "Taylor", "email": "david.taylor@email.com", "spent": 1456.73},
            {"first_name": "Jessica", "last_name": "Martinez", "email": "jessica.martinez@email.com", "spent": 589.45},
            {"first_name": "Robert", "last_name": "Garcia", "email": "robert.garcia@email.com", "spent": 2105.89},
            {"first_name": "Ashley", "last_name": "Rodriguez", "email": "ashley.rodriguez@email.com", "spent": 734.62},
            {"first_name": "Christopher", "last_name": "Lee", "email": "christopher.lee@email.com", "spent": 1823.45},
            {"first_name": "Amanda", "last_name": "White", "email": "amanda.white@email.com", "spent": 967.21},
            {"first_name": "Daniel", "last_name": "Harris", "email": "daniel.harris@email.com", "spent": 1134.78},
            {"first_name": "Jennifer", "last_name": "Clark", "email": "jennifer.clark@email.com", "spent": 845.33},
            {"first_name": "Matthew", "last_name": "Lewis", "email": "matthew.lewis@email.com", "spent": 692.84},
            {"first_name": "Nicole", "last_name": "Walker", "email": "nicole.walker@email.com", "spent": 1567.92}
        ]
        
        customers = []
        for i, template in enumerate(customer_templates, 1):
            created_date = base_date + timedelta(days=random.randint(0, 45))
            last_order_date = created_date + timedelta(days=random.randint(5, 30))
            
            customers.append({
                "id": 5000000000000 + i,
                "email": template["email"],
                "accepts_marketing": random.choice([True, False]),
                "created_at": created_date.isoformat() + "Z",
                "updated_at": last_order_date.isoformat() + "Z",
                "first_name": template["first_name"],
                "last_name": template["last_name"],
                "orders_count": random.randint(1, 8),
                "state": "enabled",
                "total_spent": str(template["spent"]),
                "last_order_id": 6000000000000 + random.randint(1, 100),
                "note": None,
                "verified_email": True,
                "multipass_identifier": None,
                "tax_exempt": False,
                "phone": f"+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}",
                "tags": "VIP, Loyal Customer" if template["spent"] > 1000 else "Regular Customer",
                "last_order_name": f"#{random.randint(1001, 9999)}",
                "currency": "USD",
                "addresses": [{
                    "id": 7000000000000 + i,
                    "customer_id": 5000000000000 + i,
                    "first_name": template["first_name"],
                    "last_name": template["last_name"],
                    "company": None,
                    "address1": f"{random.randint(100, 999)} Main St",
                    "address2": None,
                    "city": random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]),
                    "province": random.choice(["NY", "CA", "IL", "TX", "AZ"]),
                    "country": "United States",
                    "zip": f"{random.randint(10000, 99999)}",
                    "phone": f"+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}",
                    "name": f"{template['first_name']} {template['last_name']}",
                    "province_code": random.choice(["NY", "CA", "IL", "TX", "AZ"]),
                    "country_code": "US",
                    "country_name": "United States",
                    "default": True
                }],
                "admin_graphql_api_id": f"gid://shopify/Customer/{5000000000000 + i}",
                "default_address": {
                    "id": 7000000000000 + i,
                    "customer_id": 5000000000000 + i,
                    "first_name": template["first_name"],
                    "last_name": template["last_name"],
                    "company": None,
                    "address1": f"{random.randint(100, 999)} Main St",
                    "address2": None,
                    "city": random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]),
                    "province": random.choice(["NY", "CA", "IL", "TX", "AZ"]),
                    "country": "United States",
                    "zip": f"{random.randint(10000, 99999)}",
                    "phone": f"+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}",
                    "name": f"{template['first_name']} {template['last_name']}",
                    "province_code": random.choice(["NY", "CA", "IL", "TX", "AZ"]),
                    "country_code": "US",
                    "country_name": "United States",
                    "default": True
                }
            })
        
        return {"customers": customers}
    
    @staticmethod
    def get_orders_response():
        """Mock /admin/api/2023-10/orders.json response"""
        base_date = datetime.now() - timedelta(days=45)
        
        orders = []
        for i in range(1, 76):  # Generate 75 orders
            order_date = base_date + timedelta(days=random.randint(0, 40))
            
            # Random order value between $25-$400
            total_price = round(random.uniform(25.0, 400.0), 2)
            
            orders.append({
                "id": 6000000000000 + i,
                "admin_graphql_api_id": f"gid://shopify/Order/{6000000000000 + i}",
                "app_id": None,
                "browser_ip": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
                "buyer_accepts_marketing": random.choice([True, False]),
                "cart_token": f"c1-{random.randint(100000, 999999)}",
                "checkout_id": 8000000000000 + i,
                "checkout_token": f"checkout_{random.randint(100000, 999999)}",
                "client_details": {
                    "accept_language": "en-US,en;q=0.9",
                    "browser_height": random.randint(800, 1200),
                    "browser_ip": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
                    "browser_width": random.randint(1200, 1920),
                    "session_hash": None,
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                },
                "closed_at": None,
                "confirmed": True,
                "contact_email": f"customer{i}@email.com",
                "created_at": order_date.isoformat() + "Z",
                "currency": "USD",
                "current_subtotal_price": str(total_price * 0.9),  # Before tax
                "current_subtotal_price_set": {
                    "shop_money": {"amount": str(total_price * 0.9), "currency_code": "USD"},
                    "presentment_money": {"amount": str(total_price * 0.9), "currency_code": "USD"}
                },
                "current_total_discounts": "0.00",
                "current_total_discounts_set": {
                    "shop_money": {"amount": "0.00", "currency_code": "USD"},
                    "presentment_money": {"amount": "0.00", "currency_code": "USD"}
                },
                "current_total_duties_set": None,
                "current_total_price": str(total_price),
                "current_total_price_set": {
                    "shop_money": {"amount": str(total_price), "currency_code": "USD"},
                    "presentment_money": {"amount": str(total_price), "currency_code": "USD"}
                },
                "current_total_tax": str(round(total_price * 0.1, 2)),  # 10% tax
                "current_total_tax_set": {
                    "shop_money": {"amount": str(round(total_price * 0.1, 2)), "currency_code": "USD"},
                    "presentment_money": {"amount": str(round(total_price * 0.1, 2)), "currency_code": "USD"}
                },
                "customer_locale": "en",
                "device_id": None,
                "discount_codes": [],
                "email": f"customer{i}@email.com",
                "estimated_taxes": False,
                "financial_status": random.choice(["paid", "pending", "authorized"]),
                "fulfillment_status": random.choice(["fulfilled", "partial", None]),
                "gateway": "manual",
                "landing_site": "/",
                "landing_site_ref": None,
                "location_id": None,
                "name": f"#{1000 + i}",
                "note": None,
                "note_attributes": [],
                "number": 1000 + i,
                "order_number": 1000 + i,
                "order_status_url": f"https://xeno-demo-store.myshopify.com/{random.randint(100000, 999999)}/orders/{random.randint(100000, 999999)}/authenticate?key={random.randint(100000, 999999)}",
                "original_total_duties_set": None,
                "payment_gateway_names": ["manual"],
                "phone": None,
                "presentment_currency": "USD",
                "processed_at": order_date.isoformat() + "Z",
                "processing_method": "direct",
                "reference": None,
                "referring_site": "",
                "source_identifier": None,
                "source_name": "web",
                "source_url": None,
                "subtotal_price": str(total_price * 0.9),
                "subtotal_price_set": {
                    "shop_money": {"amount": str(total_price * 0.9), "currency_code": "USD"},
                    "presentment_money": {"amount": str(total_price * 0.9), "currency_code": "USD"}
                },
                "tags": "",
                "tax_lines": [{
                    "price": str(round(total_price * 0.1, 2)),
                    "rate": 0.1,
                    "title": "State Tax",
                    "price_set": {
                        "shop_money": {"amount": str(round(total_price * 0.1, 2)), "currency_code": "USD"},
                        "presentment_money": {"amount": str(round(total_price * 0.1, 2)), "currency_code": "USD"}
                    }
                }],
                "taxes_included": False,
                "test": False,
                "token": f"token_{random.randint(100000, 999999)}",
                "total_discounts": "0.00",
                "total_discounts_set": {
                    "shop_money": {"amount": "0.00", "currency_code": "USD"},
                    "presentment_money": {"amount": "0.00", "currency_code": "USD"}
                },
                "total_line_items_price": str(total_price * 0.9),
                "total_line_items_price_set": {
                    "shop_money": {"amount": str(total_price * 0.9), "currency_code": "USD"},
                    "presentment_money": {"amount": str(total_price * 0.9), "currency_code": "USD"}
                },
                "total_outstanding": "0.00",
                "total_price": str(total_price),
                "total_price_set": {
                    "shop_money": {"amount": str(total_price), "currency_code": "USD"},
                    "presentment_money": {"amount": str(total_price), "currency_code": "USD"}
                },
                "total_price_usd": str(total_price),
                "total_shipping_price_set": {
                    "shop_money": {"amount": "0.00", "currency_code": "USD"},
                    "presentment_money": {"amount": "0.00", "currency_code": "USD"}
                },
                "total_tax": str(round(total_price * 0.1, 2)),
                "total_tax_set": {
                    "shop_money": {"amount": str(round(total_price * 0.1, 2)), "currency_code": "USD"},
                    "presentment_money": {"amount": str(round(total_price * 0.1, 2)), "currency_code": "USD"}
                },
                "total_tip_received": "0.00",
                "total_weight": random.randint(500, 3000),
                "updated_at": order_date.isoformat() + "Z",
                "user_id": None,
                "billing_address": {
                    "first_name": f"Customer{i}",
                    "address1": f"{random.randint(100, 999)} Billing St",
                    "phone": f"+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}",
                    "city": random.choice(["New York", "Los Angeles", "Chicago"]),
                    "zip": f"{random.randint(10000, 99999)}",
                    "province": random.choice(["NY", "CA", "IL"]),
                    "country": "United States",
                    "last_name": "Test",
                    "address2": None,
                    "company": None,
                    "latitude": random.uniform(25.0, 49.0),
                    "longitude": random.uniform(-125.0, -66.0),
                    "name": f"Customer{i} Test",
                    "country_code": "US",
                    "province_code": random.choice(["NY", "CA", "IL"])
                },
                "customer": {
                    "id": 5000000000000 + (i % 15) + 1,  # Link to customers
                    "email": f"customer{(i % 15) + 1}@email.com",
                    "accepts_marketing": random.choice([True, False]),
                    "created_at": (order_date - timedelta(days=random.randint(30, 180))).isoformat() + "Z",
                    "updated_at": order_date.isoformat() + "Z",
                    "first_name": f"Customer{(i % 15) + 1}",
                    "last_name": "Test",
                    "orders_count": random.randint(1, 5),
                    "state": "enabled",
                    "total_spent": str(round(random.uniform(100, 2000), 2)),
                    "last_order_id": 6000000000000 + i,
                    "note": None,
                    "verified_email": True,
                    "multipass_identifier": None,
                    "tax_exempt": False,
                    "phone": f"+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}",
                    "tags": "",
                    "last_order_name": f"#{1000 + i}",
                    "currency": "USD",
                    "admin_graphql_api_id": f"gid://shopify/Customer/{5000000000000 + (i % 15) + 1}"
                },
                "discount_applications": [],
                "fulfillments": [],
                "line_items": [{
                    "id": 9000000000000 + i,
                    "admin_graphql_api_id": f"gid://shopify/LineItem/{9000000000000 + i}",
                    "fulfillable_quantity": 1,
                    "fulfillment_service": "manual",
                    "fulfillment_status": None,
                    "gift_card": False,
                    "grams": random.randint(200, 1000),
                    "name": f"Sample Product {i % 10 + 1}",
                    "price": str(total_price * 0.9),
                    "price_set": {
                        "shop_money": {"amount": str(total_price * 0.9), "currency_code": "USD"},
                        "presentment_money": {"amount": str(total_price * 0.9), "currency_code": "USD"}
                    },
                    "product_exists": True,
                    "product_id": 1000000000000 + (i % 10) + 1,
                    "properties": [],
                    "quantity": 1,
                    "requires_shipping": True,
                    "sku": f"SKU-{1000 + (i % 10) + 1}",
                    "taxable": True,
                    "title": f"Sample Product {i % 10 + 1}",
                    "total_discount": "0.00",
                    "total_discount_set": {
                        "shop_money": {"amount": "0.00", "currency_code": "USD"},
                        "presentment_money": {"amount": "0.00", "currency_code": "USD"}
                    },
                    "variant_id": 2000000000000 + (i % 10) + 1,
                    "variant_inventory_management": "shopify",
                    "variant_title": "Default Title",
                    "vendor": "Xeno Demo Store",
                    "tax_lines": [{
                        "channel_liable": None,
                        "price": str(round(total_price * 0.09, 2)),
                        "price_set": {
                            "shop_money": {"amount": str(round(total_price * 0.09, 2)), "currency_code": "USD"},
                            "presentment_money": {"amount": str(round(total_price * 0.09, 2)), "currency_code": "USD"}
                        },
                        "rate": 0.1,
                        "title": "State Tax"
                    }]
                }],
                "payment_terms": None,
                "refunds": [],
                "shipping_address": {
                    "first_name": f"Customer{i}",
                    "address1": f"{random.randint(100, 999)} Shipping St",
                    "phone": f"+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}",
                    "city": random.choice(["New York", "Los Angeles", "Chicago"]),
                    "zip": f"{random.randint(10000, 99999)}",
                    "province": random.choice(["NY", "CA", "IL"]),
                    "country": "United States",
                    "last_name": "Test",
                    "address2": None,
                    "company": None,
                    "latitude": random.uniform(25.0, 49.0),
                    "longitude": random.uniform(-125.0, -66.0),
                    "name": f"Customer{i} Test",
                    "country_code": "US",
                    "province_code": random.choice(["NY", "CA", "IL"])
                },
                "shipping_lines": []
            })
        
        return {"orders": orders}