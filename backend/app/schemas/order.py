from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    shopify_order_id: str
    total_price: float
    currency: str
    created_at: datetime

class OrderCreate(OrderBase):
    tenant_id: int

class Order(OrderBase):
    id: int
    tenant_id: int

    class Config:
        from_attributes = True
