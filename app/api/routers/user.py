#from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, HTTPException, Path
from fastapi.responses import JSONResponse, Response
from app.utils.encript import pwd_encrip

from app.schemas.user import (
    UserInDB,
    CreateUser,
    PayloadUser,
    UpdateUser,
    UserComplete,
)

from app.services.user import user_service
from app.services.rol import rol_service
from app.services.users_x_rol import users_x_rol_service


router = APIRouter()


@router.get(
    "",
    response_model=List[UserInDB],
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user error"},
    },
)
async def get_all(
    *,
    payload: PayloadUser = Depends(PayloadUser),
    skip: int = Query(0),
    limit: int = Query(99999),
) -> Optional[List[UserInDB]]:

    """
    Get all the users with the specific payload.

    **Args**:
    - **payload** (PayloadUser, optional): the payload that contains the data to filter in the get the list.
    - **skip** (int, optional): skip in the search method
    - **limit** (int, optional): limit in query search

    **Returns**:
    - **List[UserInDB]**: List of city in db with the data.
    """
    users = await user_service.get_all(
        payload=payload.dict(exclude_none=True), skip=skip, limit=limit
    )
    return users


@router.get(
    "/{id}",
    response_class=JSONResponse,
    # Creo schema para obtener la data del rol y las relaciones
    response_model=UserComplete,
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user error"},
    },
)
async def by_id(id: int = Path(...)):
    # Obtengo el usuario mediante el id
    user_data = await user_service.get_byid(id=id)
    # Obtengo de la tabla intermedia que tiene las relaciones de usuario y rol, su data con el id.
    users_x_rol_data = await users_x_rol_service.get_byid(id=id)
    # Para el usuario traigo de la entidad Rol el servicio para poder acceder al getbyid (Acceder a la info de rol), obtener la info del rol por el campo foraneo ["rol_id"] que conecta a la intermedia.
    rol_data = await rol_service.get_byid(id=users_x_rol_data["rol_id"])

    # Al tener la consulta accedo a la instacia de usuario para tener sus propiedades, ingreso a obtener el rol e igualo la data a mi instacia que trae rol (["rol"])
    user_data["rol"] = rol_data
    # Al tener la consulta accedo a la instacia de usuario para tener sus propiedades, ingreso a obtener el users_x_rol e igualo la data a mi instacia que trae users_x_rol (["users_x_rol"])
    user_data["users_x_rol"] = users_x_rol_data

    if user_data is None:
        raise HTTPException(status_code=404, detail="user not found")

    return user_data


@router.post(
    "",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=201,
    responses={
        201: {"description": "user created"},
        401: {"description": "User unauthorized"},
        404: {"description": "user error"},
    },
)
async def create(new_user: CreateUser):
    user = await user_service.get_by_username(username=new_user.username)
    if user is not None:
        raise HTTPException(
            status_code=400, detail="user already exists in database")
    password = pwd_encrip(new_user.password)
    new_user.password = password
    user = await user_service.create(obj_in=new_user)
    return user


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "user update"},
        401: {"description": "User unauthorized"},
        404: {"description": "user error"},
    },
)
async def update(update_user: UpdateUser, id: int = Path(...)):
    await user_service.update(id=id, obj_in=update_user)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "user delete"},
        401: {"description": "User unauthorized"},
        404: {"description": "user error"},
    },
)
async def delete(id: int = Path(...)):
    user = await user_service.delete(id=id)
    if user == 0:
        raise HTTPException(status_code=404, detail="user not found")
