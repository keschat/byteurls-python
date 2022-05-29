from fastapi import HTTPException, Depends, Cookie, Header

from .core.database import SessionLocal

# Dependencies


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 5):
        self.q = q
        self.skip = skip
        self.limit = limit


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(
            status_code=400, detail="No Jessica token provided")


async def raise_bad_request(status_code=400, message='Bad Request'):
    raise HTTPException(status_code, detail=message)


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(q: str = Depends(query_extractor), last_query: str | None = Cookie(default=None)):
    if not q:
        return last_query
    return q
