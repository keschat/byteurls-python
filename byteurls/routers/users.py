from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from ..models import user_model
from ..schemas import user_schema

from ..core.database import engine
from ..crud import Users

from ..dependencies import get_db, raise_bad_request, common_parameters

user_model.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_users(commons: dict = Depends(common_parameters)):
    # return commons
     return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}

# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_all_users(db, skip=skip, limit=limit)
#     return users

# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise_bad_request(status_code=404, detail="User not found")
#     return db_user    

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.fetch_user_by_email(db, email=user.email)
#     if db_user:
#        raise_bad_request(status_code=400, detail="Email already registered")
#     return crud.create_new_user(db=db, user=user)

# @app.post("/users/{user_id}/bookings/", response_model=schemas.Booking)
# def create_booking_for_user(
#     user_id: int, booking: schemas.BookingCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_booking(db=db, booking=booking, user_id=user_id)