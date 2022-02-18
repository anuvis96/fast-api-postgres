from fastapi import APIRouter

from app.api.routers import (  # haul_status,; quote_status,; user_status,
    rol,
    #root,
    users_x_rol,
    user,
)

api_router = APIRouter()

#api_router.include_router(root.router)
api_router.include_router(rol.router, prefix="/rol", tags=["Rol"])
api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(users_x_rol.router, prefix="/users_x_rol", tags=["Users x Rol"])

