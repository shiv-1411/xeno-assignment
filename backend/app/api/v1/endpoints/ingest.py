from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import user as user_model
from app.services.ingestion_service import IngestionService
from app.db.session import SessionLocal
from app.api.v1.deps import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shopify/products")
def ingest_products(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    """
    Ingest products from Shopify API for the current tenant
    """
    ingestion_service = IngestionService(db, current_user.tenant)
    result = ingestion_service.ingest_products()
    return result

@router.post("/shopify/orders")
def ingest_orders(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    """
    Ingest orders from Shopify API for the current tenant
    """
    ingestion_service = IngestionService(db, current_user.tenant)
    result = ingestion_service.ingest_orders()
    return result

@router.post("/shopify/customers")
def ingest_customers(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    """
    Ingest customers from Shopify API for the current tenant
    """
    ingestion_service = IngestionService(db, current_user.tenant)
    result = ingestion_service.ingest_customers()
    return result

@router.get("/shopify/test-connection")
def test_shopify_connection(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    """
    Test connection to Shopify API for the current tenant
    """
    ingestion_service = IngestionService(db, current_user.tenant)
    result = ingestion_service.test_connection()
    return result
