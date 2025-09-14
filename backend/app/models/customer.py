from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    shopify_customer_id = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    total_spent = Column(Float)
    created_at = Column(DateTime)
    tenant_id = Column(Integer, ForeignKey("tenant.id"))
    tenant = relationship("Tenant", back_populates="customers")
