from fastapi import APIRouter, Depends

from ..dependencies import raise_bad_request, get_db, CommonQueryParams, query_or_cookie_extractor

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)], # router dependency
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise_bad_request(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


# Will have the combination of tags: ["items", "custom"].
# And it will also have both responses in the documentation, one for 404 and one for 403.
@router.put("/{item_id}", tags=["custom"], responses={403: {"description": "Operation forbidden"}},) # path dependency
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise_bad_request(
            status_code=403, detail="You can only update the item: plumbus")
    return {"item_id": item_id, "name": "The great Plumbus"}

# @router.get("/items2/")
# async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
#     return {"q_or_cookie": query_or_default}

# @router.get("/items/")
# async def read_items(state: str | None = None, commons: CommonQueryParams = Depends()):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]
#     response.update({"items": items})
#     return response
