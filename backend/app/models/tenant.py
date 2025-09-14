from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime

class Tenant(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    shopify_store_url = Column(String, unique=True, index=True)
    shopify_access_token = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    users = relationship("User", back_populates="tenant")
    products = relationship("Product", back_populates="tenant")
    orders = relationship("Order", back_populates="tenant")
    customers = relationship("Customer", back_populates="tenant")
