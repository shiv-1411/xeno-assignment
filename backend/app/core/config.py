from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Shopify Data Ingestion & Insights Service"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://user:password@localhost/db"
    SECRET_KEY: str = "a_very_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Shopify API Configuration
    USE_SHOPIFY_API: bool = False  # Toggle between mock and real API
    SHOPIFY_API_KEY: str = "your_shopify_api_key"
    SHOPIFY_API_SECRET: str = "your_shopify_api_secret"
    SHOPIFY_API_VERSION: str = "2023-10"
    
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:3001"]

    class Config:
        env_file = ".env"

settings = Settings()
