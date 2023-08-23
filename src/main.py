import uvicorn
from fastapi import FastAPI, Depends, Request, Header, HTTPException, status
from fastapi.responses import ORJSONResponse

from core import config
from core.logger import LOGGING
from api.get_full_link.base import router_get_full_link
from api.add_short_link.base import router_add_short_link
from api.del_short_link.base import router_del_short_link
from api.ping.base import router_ping_db
from api.status.base import router_status

BLACK_LIST = [
    # "127.0.0.1"
]


async def check_allowed_ip(request: Request):
    def is_ip_banned(ip):
        is_banned = ip in BLACK_LIST
        return is_banned

    if is_ip_banned(request.client.host):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


app = FastAPI(
    title=config.app_settings.app_title,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    dependencies=[Depends(check_allowed_ip)]
)
app.include_router(router_get_full_link, prefix="/get")
app.include_router(router_add_short_link, prefix="/add")
app.include_router(router_del_short_link, prefix="/del")
app.include_router(router_ping_db, prefix="/ping")
app.include_router(router_status, prefix="/status")
if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=config.PROJECT_HOST,
        port=config.PROJECT_PORT,
    )
