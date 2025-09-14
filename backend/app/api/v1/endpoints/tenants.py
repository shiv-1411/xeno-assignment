from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import tenant as tenant_schema
from app.models import tenant as tenant_model
from app.services import tenant_service
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=tenant_schema.Tenant)
def create_tenant(tenant: tenant_schema.TenantCreate, db: Session = Depends(get_db)):
    db_tenant = tenant_service.get_tenant_by_shopify_store_url(db, shopify_store_url=tenant.shopify_store_url)
    if db_tenant:
        raise HTTPException(status_code=400, detail="Shopify store already registered")
    return tenant_service.create_tenant(db=db, tenant=tenant)
