# shortener_app/main.py

# ................

import sys
# sys.path.append(r'C:\Users\john')

from fastapi import Depends, FastAPI

# ................

# from .dependencies import get_token_header
from .internal import admin
from .routers import items, users

# ................

# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    # dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

# ................

@app.get("/")
async def read_root():
    return "Welcome to the URL shortener API :)"

# ................ 🚨 🤓 😱 🎉