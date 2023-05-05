from fastapi import APIRouter

from app.api.template_v1.controllers import dashboard_controller

template_router = APIRouter()
template_router.include_router(dashboard_controller.router, tags=["dashboard"])

