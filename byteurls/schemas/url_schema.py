# shortener_app/schemas.py

from pydantic import BaseModel

# URLBase = BaseModel
class URLBase(BaseModel):
    target_url: str

# URL = URLBase
class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True

# URLInfo = URL
class URLInfo(URL):
    url: str
    admin_url: str