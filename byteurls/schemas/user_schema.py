# shortener_app/schemas.py

from pydantic import BaseModel

from .booking_schema import Booking

# USER
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    bookings: list[Booking] = []

    class Config:
        orm_mode = True