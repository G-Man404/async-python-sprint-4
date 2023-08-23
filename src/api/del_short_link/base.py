from fastapi import APIRouter
from src.db.db import del_link
from fastapi.responses import Response

router_del_short_link = APIRouter()


@router_del_short_link.get('/')
async def add_short_link(link):
    if await del_link(int(link)):
        return Response(status_code=201)
    else:
        return Response(status_code=404)
