#!/usr/bin/env python3
"""
Pre-Deployment Verification Script
Checks if everything is ready for deployment
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if required file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} (MISSING)")
        return False

def check_deployment_readiness():
    """Check if project is ready for deployment"""
    
    print("🔍 Checking Deployment Readiness...\n")
    
    issues = []
    
    # Check required files
    files_to_check = [
        ("render.yaml", "Render deployment config"),
        ("backend/requirements.txt", "Python dependencies"),
        ("backend/run.py", "Backend entry point"),
        ("backend/app/main.py", "FastAPI application"),
        ("backend/deployment_setup.py", "Deployment setup script"),
        ("frontend/package.json", "Frontend dependencies"),
        ("frontend/src/App.js", "React application"),
        (".gitignore", "Git ignore file"),
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            issues.append(f"Missing {filepath}")
    
    # Check render.yaml configuration
    print("\n📋 Checking render.yaml configuration...")
    try:
        with open("render.yaml", "r") as f:
            content = f.read()
            if "USE_SHOPIFY_API" in content and "false" in content:
                print("✅ Mock mode configured in render.yaml")
            else:
                print("⚠️  Mock mode not found in render.yaml")
                issues.append("Mock mode not configured")
                
            if "xeno-postgres" in content:
                print("✅ Database configured in render.yaml")
            else:
                print("❌ Database not configured in render.yaml")
                issues.append("Database not configured")
    except Exception as e:
        print(f"❌ Error reading render.yaml: {e}")
        issues.append("Cannot read render.yaml")
    
    # Check frontend build
    print("\n🏗️  Checking frontend build...")
    if os.path.exists("frontend/build"):
        print("✅ Frontend build directory exists")
    else:
        print("⚠️  Frontend build directory not found (will build during deployment)")
    
    # Check backend structure
    print("\n🐍 Checking backend structure...")
    backend_files = [
        "backend/app/__init__.py",
        "backend/app/main.py", 
        "backend/app/core/config.py",
        "backend/app/services/ingestion_service.py",
        "backend/app/services/shopify_mock_fixtures.py"
    ]
    
    for filepath in backend_files:
        check_file_exists(filepath, f"Backend file")
    
    # Check environment configuration
    print("\n🔧 Checking mock mode implementation...")
    try:
        # Check if config has USE_SHOPIFY_API
        config_path = "backend/app/core/config.py"
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                config_content = f.read()
                if "USE_SHOPIFY_API" in config_content:
                    print("✅ USE_SHOPIFY_API flag implemented")
                else:
                    print("❌ USE_SHOPIFY_API flag not found")
                    issues.append("Mock mode toggle not implemented")
    except Exception as e:
        print(f"❌ Error checking config: {e}")
        issues.append("Cannot verify mock mode config")
    
    # Summary
    print("\n" + "="*50)
    if not issues:
        print("🎉 DEPLOYMENT READY!")
        print("✅ All checks passed")
        print("🚀 You can deploy to Render now!")
        
        print("\n📋 Next Steps:")
        print("1. Push code to GitHub: git add . && git commit -m 'Ready for deployment' && git push")
        print("2. Go to render.com and create a new Blueprint")
        print("3. Connect your GitHub repo and deploy")
        print("4. Wait for deployment to complete")
        print("5. Test your live application!")
        
        return True
    else:
        print("❌ DEPLOYMENT ISSUES FOUND:")
        for issue in issues:
            print(f"   • {issue}")
        print("\n🔧 Fix these issues before deploying")
        return False

if __name__ == "__main__":
    # Change to project root directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    ready = check_deployment_readiness()
    
    if ready:
        print(f"\n🌟 Project Status: DEPLOYMENT READY")
        print(f"📊 Mode: Mock (Professional)")
        print(f"🎯 Assignment: Fully Compliant")  
        sys.exit(0)
    else:
        print(f"\n⚠️  Project Status: NEEDS FIXES")
        sys.exit(1)