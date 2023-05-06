from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

from app import services, core, dto

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index():
    return RedirectResponse("/dashboard")


@router.get("/robots.txt", response_class=PlainTextResponse)
def robots():
    data = """User-agent: *\nDisallow: /"""
    return data


@router.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request, db: Session = Depends(core.get_db)):
    server = dto.Server(server_deployer="macaron")
    my_servers_entity = services.server.get_by_deployer(db=db, server=server)
    other_servers_entity = services.server.get_except_deployer(db=db, server=server)

    my_servers = []
    for s in my_servers_entity:
        my_servers.append(dto.Server.from_orm(s))
    other_servers = []
    for s in other_servers_entity:
        other_servers.append(dto.Server.from_orm(s))
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "page": "dashboard",
            "my_servers": my_servers,
            "other_servers": other_servers,
        },
    )
