# shortener_app/models.py

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..core.database import Base

##BOOKING
class Booking(Base):
    __tablename__ = "bookings"

    id=Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
    description = Column(String, index=True)
    created_date = Column(DateTime, server_default=func.now())
    user_id = Column(Integer,ForeignKey("users.id"))

    owner = relationship("User",back_populates="bookings")