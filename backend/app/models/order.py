from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    shopify_order_id = Column(String, unique=True, index=True)
    total_price = Column(Float)
    currency = Column(String)
    created_at = Column(DateTime)
    tenant_id = Column(Integer, ForeignKey("tenant.id"))
    tenant = relationship("Tenant", back_populates="orders")
