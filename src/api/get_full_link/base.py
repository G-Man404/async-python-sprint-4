from fastapi import APIRouter
from fastapi import Request, status, HTTPException
from fastapi.responses import Response

from src.db.db import find_full_link, add_transition

router_get_full_link = APIRouter()


@router_get_full_link.get('/')
async def get_full_link(link, request: Request):
    full_link = await find_full_link(int(link))
    if full_link is None:
        return Response(status_code=404)
    if full_link.remove:
        return Response(status_code=410)
    await add_transition(full_link, request.client.host)
    return Response(content=full_link.full_link, status_code=201)

