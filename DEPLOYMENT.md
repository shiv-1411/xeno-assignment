# Xeno Shopify Analytics - Render Deployment

## Deploy Backend (API)
1. Create new Web Service on Render
2. Connect your GitHub repository
3. Use these settings:
   - **Name**: xeno-shopify-api
   - **Environment**: Docker
   - **Region**: Oregon (US West)
   - **Branch**: main
   - **Root Directory**: backend
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python run.py`

## Environment Variables for Backend
```
DATABASE_URL=postgresql://username:password@hostname:port/database
SECRET_KEY=your-super-secret-key-here
API_V1_STR=/api/v1
SHOPIFY_API_VERSION=2023-10
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Deploy Frontend
1. Create new Static Site on Render
2. Connect your GitHub repository
3. Use these settings:
   - **Name**: xeno-shopify-dashboard
   - **Environment**: Static Site
   - **Root Directory**: frontend
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: build

## Environment Variables for Frontend
```
REACT_APP_API_URL=https://xeno-shopify-api.onrender.com
```

## PostgreSQL Database
1. Create PostgreSQL database on Render
2. Copy the connection string to backend environment variables

## Post-Deployment Steps
1. Run database creation: `https://your-api-url.onrender.com/docs`
2. Use the create_tables.py script via the API docs
3. Run sample data population
4. Test login with sample credentials

## Free Tier Limitations
- Backend: 512MB RAM, goes to sleep after 15 min inactivity
- Database: 1GB storage, 97 connection limit
- Frontend: Unlimited bandwidth

## Production URLs (Once Deployed)
- **Frontend**: https://xeno-shopify-dashboard.onrender.com
- **Backend API**: https://xeno-shopify-api.onrender.com
- **API Docs**: https://xeno-shopify-api.onrender.com/docs
