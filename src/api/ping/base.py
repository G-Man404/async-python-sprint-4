from fastapi import APIRouter
from fastapi.responses import Response

from src.db.db import ping
router_ping_db = APIRouter()


@router_ping_db.get('/')
async def ping_db():
    if await ping():
        return Response(status_code=201)
    else:
        return Response(status_code=500)