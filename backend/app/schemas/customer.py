from pydantic import BaseModel
from datetime import datetime

class CustomerBase(BaseModel):
    shopify_customer_id: str
    first_name: str
    last_name: str
    email: str
    total_spent: float

class CustomerCreate(CustomerBase):
    tenant_id: int
    created_at: datetime

class Customer(CustomerBase):
    id: int
    tenant_id: int
    created_at: datetime

    class Config:
        from_attributes = True
