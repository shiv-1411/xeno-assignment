# 🛍️ Shopify Development Store Setup Guide

## Step 1: Create Shopify Partner Account
1. Go to [partners.shopify.com](https://partners.shopify.com)
2. Sign up for a free Shopify Partner account
3. Verify your email address

## Step 2: Create Development Store
1. Log into your Partner Dashboard
2. Click "Stores" → "Add store"
3. Choose "Development store"
4. Fill in store details:
   - **Store name**: `xeno-demo-store`
   - **Store URL**: `xeno-demo-store.myshopify.com`
   - **Purpose**: Development
   - **Build for**: Myself
5. Click "Save"

## Step 3: Create Shopify App
1. In Partner Dashboard, go to "Apps" → "Create app"
2. Choose "Create app manually"
3. Fill in app details:
   - **App name**: `Xeno Analytics Integration`
   - **App URL**: `http://localhost:8000` (for local development)
   - **Allowed redirection URLs**: `http://localhost:3000/auth/callback` (for local development)
4. Click "Create app"

> 💡 **Local Development**: Use `localhost` URLs for initial testing. Update to production URLs when deploying.

## Step 4: Configure App Permissions
In your app settings, add these scopes:
- `read_customers` - Read customer data
- `read_orders` - Read order data  
- `read_products` - Read product data
- `read_inventory` - Read inventory data
- `write_webhooks` - Create webhooks for real-time sync

## Step 5: Install App to Development Store
1. In your app dashboard, click "Select store"
2. Choose your development store
3. Click "Install" to install the app
4. Copy the **Access Token** - you'll need this for API calls

## Step 6: Add Sample Data to Store
### Products (Add 10-15 products):
```
1. Premium T-Shirt - $29.99 - Fashion
2. Wireless Earbuds - $89.99 - Electronics  
3. Coffee Mug - $19.99 - Home & Kitchen
4. Yoga Mat - $49.99 - Sports & Fitness
5. Phone Case - $24.99 - Electronics
6. Notebook - $12.99 - Office Supplies
7. Water Bottle - $34.99 - Sports & Fitness
8. Desk Lamp - $79.99 - Home & Kitchen
9. Backpack - $69.99 - Fashion
10. Bluetooth Speaker - $129.99 - Electronics
```

### Customers (Add 8-10 customers):
```
1. John Smith - john.smith@email.com
2. Sarah Johnson - sarah.johnson@email.com  
3. Mike Brown - mike.brown@email.com
4. Lisa Davis - lisa.davis@email.com
5. David Wilson - david.wilson@email.com
6. Emma Taylor - emma.taylor@email.com
7. Chris Anderson - chris.anderson@email.com
8. Amanda White - amanda.white@email.com
```

### Orders (Create 15-20 test orders):
- Vary order dates over last 2 months
- Mix of different products and quantities
- Different order statuses (paid, pending, cancelled)
- Range of order values ($25 - $300)

## Step 7: API Configuration
Update your backend `.env` file with real Shopify credentials:

```env
# Shopify Configuration
SHOPIFY_API_KEY=your_app_api_key
SHOPIFY_API_SECRET=your_app_secret
SHOPIFY_ACCESS_TOKEN=your_store_access_token
SHOPIFY_STORE_URL=xeno-demo-store.myshopify.com
SHOPIFY_API_VERSION=2023-10
SHOPIFY_WEBHOOK_SECRET=your_webhook_secret
```

## Step 8: Test API Connection
Run this test script to verify connection:

```python
import requests

# Test connection to your Shopify store
headers = {
    'X-Shopify-Access-Token': 'your_access_token_here'
}

# Test products endpoint
response = requests.get(
    'https://xeno-demo-store.myshopify.com/admin/api/2023-10/products.json',
    headers=headers
)

if response.status_code == 200:
    print("✅ Successfully connected to Shopify!")
    print(f"Found {len(response.json()['products'])} products")
else:
    print("❌ Connection failed:", response.status_code)
```

## Step 9: Configure Webhooks (Optional)
For real-time data sync, set up webhooks:

1. **Order Creation**: `https://your-api-url.onrender.com/api/v1/webhooks/orders/create`
2. **Customer Update**: `https://your-api-url.onrender.com/api/v1/webhooks/customers/update`  
3. **Product Update**: `https://your-api-url.onrender.com/api/v1/webhooks/products/update`

## Step 10: Update Ingestion Service
Replace the sample data ingestion with real Shopify API calls:

```python
# In app/services/ingestion_service.py
def ingest_products(self):
    url = f"{self.base_url}/products.json"
    response = requests.get(url, headers=self.headers)
    
    if response.status_code == 200:
        products = response.json().get("products", [])
        for product_data in products:
            # Process and store real Shopify product data
            self._create_or_update_product(product_data)
    else:
        print(f"Error fetching products: {response.status_code}")
```

## 🎯 Expected Results
After setup, you should have:
- ✅ Working Shopify development store with sample data
- ✅ Shopify app with proper permissions
- ✅ API credentials for data ingestion
- ✅ Real product, customer, and order data
- ✅ Working webhook endpoints (optional)

## 🚨 Important Notes
- Development stores are free but have limitations
- Access tokens expire - implement refresh logic for production
- Rate limiting: Max 40 requests/second to Shopify APIs
- Webhook verification is crucial for security

## 📞 Support Resources  
- [Shopify API Documentation](https://shopify.dev/api)
- [Partner Dashboard](https://partners.shopify.com)
- [Shopify Community Forums](https://community.shopify.com)
