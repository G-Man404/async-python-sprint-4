from fastapi import APIRouter, Depends
from fastapi.responses import Response
from typing import Union, Annotated

from src.db.db import get_transitions
router_status = APIRouter()


async def paginator_response():
    return {
        "offset": 0,
        "max-result": 3,
        "full-info": False
    }


@router_status.post('/')
async def status(link, full: bool = False, offset: int = 0, max: int = 10):
    transitions = await get_transitions(int(link))
    if not full:
        return len(transitions)
    else:
        new_trans = transitions[offset: offset+max]
        return new_trans
