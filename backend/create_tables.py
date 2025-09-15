#!/usr/bin/env python3
"""
Script to create all database tables directly using SQLAlchemy.
This bypasses Alembic for initial setup.
"""
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from sqlalchemy import create_engine
from app.core.config import settings
from app.db.base import Base

def create_tables():
    """Create all database tables."""
    from app.db.session import engine, ensure_schema_exists
    
    # Ensure schema exists first
    ensure_schema_exists()
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("All database tables created successfully!")
    print(f"Schema: {settings.DATABASE_SCHEMA}")

if __name__ == "__main__":
    create_tables()
