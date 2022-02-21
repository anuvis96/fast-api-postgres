from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.users_x_rol import (
    CreateUsersXRol,
    SearchUsersXRol,
    UsersXRol,
)
from app.services.rol import rol_service
from app.services.user import user_service
from app.services.users_x_rol import users_x_rol_service

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[UsersXRol],
    status_code=200,
    responses={
        200: {"description": "Users per rol found"},
        401: {"description": "user unauthorized"},
        404: {"description": "users per rol error"},
    },
)
async def get_all_relation(
    skip: int = Query(0),
    limit: int = Query(99999),
    search: SearchUsersXRol = Depends(SearchUsersXRol),
):
    user_banks = await users_x_rol_service.get_all(
        skip=skip,
        limit=limit,
        payload=search.dict(exclude_none=True),
    )
    return user_banks


@router.post(
    "/user/{user_id}/rol/{rol_id}",
    response_class=JSONResponse,
    status_code=201,
    responses={
        201: {"description": "User per rol created"},
        401: {"description": "user unauthorized"},
        404: {"description": "users per rol error"},
    },
)
async def add_rol_to_user(user_id: int, rol_id: int):
    get_rol = await rol_service.get_byid(id=rol_id)
    if get_rol is None:
        raise HTTPException(status_code=404, detail=f"rol {rol_id} not found")
    get_user = await user_service.get_byid(id=user_id)
    if get_user is None:
        raise HTTPException(status_code=404, detail=f"user {user_id} not found")
    relation = CreateUsersXRol(user_id=user_id, rol_id=rol_id)
    await users_x_rol_service.create(obj_in=relation)
    rol_new = await users_x_rol_service.get_relation_by_user(user_id=user_id)
    return rol_new


@router.post(
    "/rol/{rol_id}/user/{user_id}",
    response_class=JSONResponse,
    status_code=201,
    responses={
        201: {"description": "Rol per user created"},
        401: {"description": "user unauthorized"},
        404: {"description": "rol per user error"},
    },
)
async def add_user_to_rol(user_id: int, rol_id: int):
    get_rol = await rol_service.get_byid(id=rol_id)
    if get_rol is None:
        raise HTTPException(status_code=404, detail=f"rol {rol_id} not found")
    get_user = await user_service.get_byid(id=user_id)
    if get_user is None:
        raise HTTPException(status_code=404, detail=f"user {user_id} not found")
    relation = CreateUsersXRol(user_id=user_id, rol_id=rol_id)
    await users_x_rol_service.create(obj_in=relation)
    bank_new = await users_x_rol_service.get_relation_by_rol(rol_id=rol_id)
    return bank_new