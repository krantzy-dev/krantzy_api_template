from fastapi import APIRouter

from src.routes.health import router as health_router

api_router = APIRouter()
api_router.include_router(health_router)

# add future Routers here:
# api_router.include_router(<your_router>)