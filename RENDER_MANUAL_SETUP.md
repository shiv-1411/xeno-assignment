# Render Manual Deployment Settings for Backend

## Service Configuration:
- **Name**: xeno-shopify-api
- **Environment**: Python 3
- **Build Command**: pip install -r requirements.txt
- **Start Command**: python run.py
- **Instance Type**: Free

## Environment Variables:
USE_SHOPIFY_API=false
SECRET_KEY=your_generated_secret_key_here
API_V1_STR=/api/v1
SHOPIFY_API_VERSION=2023-10
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

## Advanced Settings:
- **Root Directory**: backend
- **Auto-Deploy**: Yes
- **Health Check Path**: /health

## Database (Add after service is created):
1. Create PostgreSQL database (Free)
2. Copy connection string to DATABASE_URL env var