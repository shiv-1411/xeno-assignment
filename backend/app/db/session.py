from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create engine with schema configuration
engine_url = settings.DATABASE_URL
if settings.DATABASE_SCHEMA:
    # Add schema to connection options
    engine = create_engine(
        engine_url, 
        pool_pre_ping=True,
        connect_args={"options": f"-csearch_path={settings.DATABASE_SCHEMA},public"}
    )
else:
    engine = create_engine(engine_url, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to ensure schema exists
def ensure_schema_exists():
    """Ensure the specified schema exists in the database."""
    if settings.DATABASE_SCHEMA and settings.DATABASE_SCHEMA != "public":
        with engine.connect() as connection:
            connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {settings.DATABASE_SCHEMA}"))
            connection.commit()
