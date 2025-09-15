#!/usr/bin/env python3
"""
Simple startup script for Render deployment
This ensures proper path handling and environment setup
"""

import os
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

# Set working directory  
os.chdir(backend_dir)

# Import and run the app
if __name__ == "__main__":
    import uvicorn
    from app.main import app
    
    # Get port from environment (Render sets this)
    port = int(os.environ.get("PORT", 8000))
    
    print(f"🚀 Starting Xeno Shopify Analytics API on port {port}")
    print(f"📊 Mock Mode: {os.environ.get('USE_SHOPIFY_API', 'false') == 'false'}")
    
    # Run the application
    uvicorn.run(app, host="0.0.0.0", port=port)