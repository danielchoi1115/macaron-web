from fastapi import APIRouter

from app.api.api_v1.controllers import server_controller

api_router = APIRouter()

api_router.include_router(server_controller.router, prefix="/server", tags=["server"])
