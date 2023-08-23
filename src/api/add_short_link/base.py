from fastapi import APIRouter
from fastapi import Request
from src.db.db import find_short_link, add_link
router_add_short_link = APIRouter()


@router_add_short_link.post('/')
async def add_short_link(request: Request, link):
    short_link = await find_short_link(link)
    if short_link is None:
        short_link = await add_link(link, request.client.host)
    return short_link.id

