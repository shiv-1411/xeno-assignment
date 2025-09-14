from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    tenant_id = Column(Integer, ForeignKey("tenant.id"))
    tenant = relationship("Tenant", back_populates="users")

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.hashed_password)

    def hash_password(self, password):
        self.hashed_password = pwd_context.hash(password)
