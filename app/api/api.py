from fastapi import APIRouter

from app.api.endpoints import (  # haul_status,; quote_status,; user_status,
    #rol,
    #root,
    user,
)

api_router = APIRouter()

#api_router.include_router(root.router)
#api_router.include_router(rol.router, prefix="/rol", tags=["rol"])
api_router.include_router(user.router, prefix="/user", tags=["user"])

