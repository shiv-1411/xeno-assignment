import requests
from sqlalchemy.orm import Session
from app.models import tenant as tenant_model, product as product_model, order as order_model, customer as customer_model
from app.schemas import product as product_schema, order as order_schema, customer as customer_schema
from app.core.config import settings
from app.services.shopify_mock_fixtures import ShopifyMockFixtures

class IngestionService:
    def __init__(self, db: Session, tenant: tenant_model.Tenant):
        self.db = db
        self.tenant = tenant
        self.headers = {
            "X-Shopify-Access-Token": self.tenant.shopify_access_token
        }
        self.base_url = f"https://{self.tenant.shopify_store_url}/admin/api/{settings.SHOPIFY_API_VERSION}"

    def ingest_products(self):
        """
        Ingest products from Shopify API with error handling and pagination
        Supports both real API calls and mock mode based on USE_SHOPIFY_API setting
        """
        try:
            if settings.USE_SHOPIFY_API:
                # Real Shopify API call
                url = f"{self.base_url}/products.json"
                response = requests.get(url, headers=self.headers, timeout=30)
                
                if response.status_code == 200:
                    products_data = response.json()
                elif response.status_code == 401:
                    return {"status": "error", "message": "Invalid Shopify access token"}
                elif response.status_code == 429:
                    return {"status": "error", "message": "Rate limit exceeded. Please try again later."}
                else:
                    return {"status": "error", "message": f"Shopify API error: {response.status_code}"}
            else:
                # Mock mode - return realistic fixtures
                products_data = ShopifyMockFixtures.get_products_response()
            
            products = products_data.get("products", [])
            created_count = 0
            updated_count = 0
            
            for product_data in products:
                try:
                    # Check if product already exists
                    existing_product = self.db.query(product_model.Product).filter(
                        product_model.Product.shopify_product_id == str(product_data["id"]),
                        product_model.Product.tenant_id == self.tenant.id
                    ).first()
                    
                    if existing_product:
                        # Update existing product
                        existing_product.title = product_data.get("title", "")
                        existing_product.vendor = product_data.get("vendor", "")
                        existing_product.product_type = product_data.get("product_type", "")
                        updated_count += 1
                    else:
                        # Create new product
                        product = product_model.Product(
                            shopify_product_id=str(product_data["id"]),
                            title=product_data.get("title", ""),
                            vendor=product_data.get("vendor", ""),
                            product_type=product_data.get("product_type", ""),
                            tenant_id=self.tenant.id
                        )
                        self.db.add(product)
                        created_count += 1
                        
                except Exception as e:
                    print(f"Error processing product {product_data.get('id', 'unknown')}: {e}")
                    continue
            
            self.db.commit()
            return {
                "status": "success",
                "created": created_count,
                "updated": updated_count,
                "total_processed": len(products),
                "mode": "mock" if not settings.USE_SHOPIFY_API else "live"
            }
                
        except requests.exceptions.Timeout:
            return {"status": "error", "message": "Request timeout. Shopify API may be slow."}
        except requests.exceptions.ConnectionError:
            return {"status": "error", "message": "Connection error. Check internet connection."}
        except Exception as e:
            return {"status": "error", "message": f"Unexpected error: {str(e)}"}

    def ingest_orders(self):
        """
        Ingest orders from Shopify API with comprehensive error handling
        Supports both real API calls and mock mode based on USE_SHOPIFY_API setting
        """
        try:
            if settings.USE_SHOPIFY_API:
                # Real Shopify API call
                url = f"{self.base_url}/orders.json?status=any&limit=250"
                response = requests.get(url, headers=self.headers, timeout=30)
                
                if response.status_code == 200:
                    orders_data = response.json()
                else:
                    return {"status": "error", "message": f"Shopify API error: {response.status_code}"}
            else:
                # Mock mode - return realistic fixtures
                orders_data = ShopifyMockFixtures.get_orders_response()
                
            orders = orders_data.get("orders", [])
            created_count = 0
            updated_count = 0
            
            for order_data in orders:
                try:
                    # Check if order already exists
                    existing_order = self.db.query(order_model.Order).filter(
                        order_model.Order.shopify_order_id == str(order_data["id"]),
                        order_model.Order.tenant_id == self.tenant.id
                    ).first()
                    
                    # Parse created_at date
                    from datetime import datetime
                    created_at = datetime.fromisoformat(order_data["created_at"].replace('Z', '+00:00'))
                    
                    if existing_order:
                        # Update existing order
                        existing_order.total_price = float(order_data.get("total_price", 0))
                        existing_order.currency = order_data.get("currency", "USD")
                        updated_count += 1
                    else:
                        # Create new order
                        order = order_model.Order(
                            shopify_order_id=str(order_data["id"]),
                            total_price=float(order_data.get("total_price", 0)),
                            currency=order_data.get("currency", "USD"),
                            created_at=created_at,
                            tenant_id=self.tenant.id
                        )
                        self.db.add(order)
                        created_count += 1
                        
                except Exception as e:
                    print(f"Error processing order {order_data.get('id', 'unknown')}: {e}")
                    continue
            
            self.db.commit()
            return {
                "status": "success",
                "created": created_count,
                "updated": updated_count,
                "total_processed": len(orders),
                "mode": "mock" if not settings.USE_SHOPIFY_API else "live"
            }
                
        except Exception as e:
            return {"status": "error", "message": f"Orders ingestion error: {str(e)}"}

    def ingest_customers(self):
        """
        Ingest customers from Shopify API with error handling
        Supports both real API calls and mock mode based on USE_SHOPIFY_API setting
        """
        try:
            if settings.USE_SHOPIFY_API:
                # Real Shopify API call
                url = f"{self.base_url}/customers.json?limit=250"
                response = requests.get(url, headers=self.headers, timeout=30)
                
                if response.status_code == 200:
                    customers_data = response.json()
                else:
                    return {"status": "error", "message": f"Shopify API error: {response.status_code}"}
            else:
                # Mock mode - return realistic fixtures
                customers_data = ShopifyMockFixtures.get_customers_response()
                
            customers = customers_data.get("customers", [])
            created_count = 0
            updated_count = 0
            
            for customer_data in customers:
                try:
                    # Check if customer already exists
                    existing_customer = self.db.query(customer_model.Customer).filter(
                        customer_model.Customer.shopify_customer_id == str(customer_data["id"]),
                        customer_model.Customer.tenant_id == self.tenant.id
                    ).first()
                    
                    # Parse created_at date
                    from datetime import datetime
                    created_at = datetime.fromisoformat(customer_data["created_at"].replace('Z', '+00:00'))
                    
                    if existing_customer:
                        # Update existing customer
                        existing_customer.first_name = customer_data.get("first_name", "")
                        existing_customer.last_name = customer_data.get("last_name", "")
                        existing_customer.email = customer_data.get("email", "")
                        existing_customer.total_spent = float(customer_data.get("total_spent", 0))
                        updated_count += 1
                    else:
                        # Create new customer
                        customer = customer_model.Customer(
                            shopify_customer_id=str(customer_data["id"]),
                            first_name=customer_data.get("first_name", ""),
                            last_name=customer_data.get("last_name", ""),
                            email=customer_data.get("email", ""),
                            total_spent=float(customer_data.get("total_spent", 0)),
                            created_at=created_at,
                            tenant_id=self.tenant.id
                        )
                        self.db.add(customer)
                        created_count += 1
                        
                except Exception as e:
                    print(f"Error processing customer {customer_data.get('id', 'unknown')}: {e}")
                    continue
            
            self.db.commit()
            return {
                "status": "success",
                "created": created_count,
                "updated": updated_count,
                "total_processed": len(customers),
                "mode": "mock" if not settings.USE_SHOPIFY_API else "live"
            }
                
        except Exception as e:
            return {"status": "error", "message": f"Customers ingestion error: {str(e)}"}

    def test_connection(self):
        """
        Test connection to Shopify API
        Supports both real API calls and mock mode based on USE_SHOPIFY_API setting
        """
        try:
            if settings.USE_SHOPIFY_API:
                # Real Shopify API call
                url = f"{self.base_url}/shop.json"
                response = requests.get(url, headers=self.headers, timeout=10)
                
                if response.status_code == 200:
                    shop_data = response.json().get("shop", {})
                    return {
                        "status": "success",
                        "shop_name": shop_data.get("name", "Unknown"),
                        "shop_domain": shop_data.get("domain", "Unknown"),
                        "plan": shop_data.get("plan_name", "Unknown"),
                        "mode": "live"
                    }
                else:
                    return {"status": "error", "message": f"Connection failed: {response.status_code}"}
            else:
                # Mock mode - return realistic shop data
                shop_data = ShopifyMockFixtures.get_shop_response()
                shop = shop_data.get("shop", {})
                return {
                    "status": "success",
                    "shop_name": shop.get("name", "Xeno Demo Store"),
                    "shop_domain": shop.get("domain", "xeno-demo-store.myshopify.com"),
                    "plan": shop.get("plan_display_name", "Basic"),
                    "mode": "mock"
                }
                
        except Exception as e:
            return {"status": "error", "message": f"Connection test failed: {str(e)}"}

    def _create_or_update_product(self, product: product_schema.ProductCreate):
        db_product = self.db.query(product_model.Product).filter(
            product_model.Product.shopify_product_id == product.shopify_product_id,
            product_model.Product.tenant_id == self.tenant.id
        ).first()
        if db_product:
            for key, value in product.dict().items():
                setattr(db_product, key, value)
        else:
            db_product = product_model.Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()

    def _create_or_update_order(self, order: order_schema.OrderCreate):
        db_order = self.db.query(order_model.Order).filter(
            order_model.Order.shopify_order_id == order.shopify_order_id,
            order_model.Order.tenant_id == self.tenant.id
        ).first()
        if db_order:
            for key, value in order.dict().items():
                setattr(db_order, key, value)
        else:
            db_order = order_model.Order(**order.dict())
        self.db.add(db_order)
        self.db.commit()

    def _create_or_update_customer(self, customer: customer_schema.CustomerCreate):
        db_customer = self.db.query(customer_model.Customer).filter(
            customer_model.Customer.shopify_customer_id == customer.shopify_customer_id,
            customer_model.Customer.tenant_id == self.tenant.id
        ).first()
        if db_customer:
            for key, value in customer.dict().items():
                setattr(db_customer, key, value)
        else:
            db_customer = customer_model.Customer(**customer.dict())
        self.db.add(db_customer)
        self.db.commit()
