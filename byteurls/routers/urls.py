from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import secrets
import validators

from ..dependencies import get_db, raise_bad_request

from models import url_model
from schemas import url_schema

from core.database import SessionLocal, engine

url_model.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/url",
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=url_schema.URLInfo)
async def create_url(url: url_schema.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = url_model.URL(target_url=url.target_url,
                           key=key, secret_key=secret_key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url