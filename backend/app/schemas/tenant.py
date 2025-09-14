from pydantic import BaseModel
from typing import Optional

class TenantBase(BaseModel):
    name: str
    shopify_store_url: str

class TenantCreate(TenantBase):
    shopify_access_token: str

class Tenant(TenantBase):
    id: int
    shopify_access_token: Optional[str] = None

    class Config:
        from_attributes = True
