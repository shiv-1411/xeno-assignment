from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    shopify_product_id = Column(String, unique=True, index=True)
    title = Column(String)
    vendor = Column(String)
    product_type = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    tenant_id = Column(Integer, ForeignKey("tenant.id"))
    tenant = relationship("Tenant", back_populates="products")
