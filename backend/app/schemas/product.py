from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    shopify_product_id: str
    title: str
    vendor: str
    product_type: str

class ProductCreate(ProductBase):
    tenant_id: int

class Product(ProductBase):
    id: int
    tenant_id: int
    created_at: datetime

    class Config:
        from_attributes = True
