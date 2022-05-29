# shortener_app/models.py

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..core.database import Base

##USER
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)
    email = Column(String, unique=True, index= True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)

    bookings = relationship("Booking", back_populates="owner")