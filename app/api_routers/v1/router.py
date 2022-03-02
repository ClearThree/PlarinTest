from fastapi import APIRouter

from app.api_routers.v1.employees.employees_router import employees_router


v1router = APIRouter(prefix="/v1", tags=["v1"])
v1router.include_router(employees_router)
