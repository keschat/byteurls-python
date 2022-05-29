from pydantic import BaseModel

# BOOKING
class BookingBase(BaseModel):
    name: str
    description: str = None

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True