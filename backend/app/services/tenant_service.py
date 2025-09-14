from sqlalchemy.orm import Session
from app.models import tenant as tenant_model
from app.schemas import tenant as tenant_schema

def get_tenant(db: Session, tenant_id: int):
    return db.query(tenant_model.Tenant).filter(tenant_model.Tenant.id == tenant_id).first()

def get_tenant_by_shopify_store_url(db: Session, shopify_store_url: str):
    return db.query(tenant_model.Tenant).filter(tenant_model.Tenant.shopify_store_url == shopify_store_url).first()

def create_tenant(db: Session, tenant: tenant_schema.TenantCreate):
    db_tenant = tenant_model.Tenant(
        name=tenant.name,
        shopify_store_url=tenant.shopify_store_url,
        shopify_access_token=tenant.shopify_access_token
    )
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant
