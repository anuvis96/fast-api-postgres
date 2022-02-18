#from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, HTTPException, Path
from fastapi.responses import JSONResponse, Response
from app.utils.encript import pwd_encrip

from app.schemas.rol import (
    RolInDB,
    CreateRol,
    PayloadRol,
    UpdateRol,
)

from app.services.rol import rol_service


router = APIRouter()


@router.get(
    "",
    response_model=List[RolInDB],
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "Rol found"},
        401: {"description": "user unauthorized"},
        404: {"description": "rol error"},
    },
)
async def get_all(
    *,
    payload: PayloadRol = Depends(PayloadRol),
    skip: int = Query(0),
    limit: int = Query(99999),
) -> Optional[List[RolInDB]]:

    """
    Get all the rol with the specific payload.

    **Args**:
    - **payload** (PayloadUser, optional): the payload that contains the data to filter in the get the list.
    - **skip** (int, optional): skip in the search method
    - **limit** (int, optional): limit in query search

    **Returns**:
    - **List[UserInDB]**: List of city in db with the data.
    """
    rols = await rol_service.get_all(
        payload=payload.dict(exclude_none=True), skip=skip, limit=limit
    )
    return rols


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=RolInDB,
    status_code=200,
    responses={
        200: {"description": "Rol found"},
        401: {"description": "user unauthorized"},
        404: {"description": "rol error"},
    },
)
async def by_id(id: int = Path(...)):
    user = await rol_service.get_byid(id=id)
    if user is None:
        raise HTTPException(status_code=404, detail="rol not found")
    return user


@router.post(
    "",
    response_class=JSONResponse,
    response_model=RolInDB,
    status_code=201,
    responses={
        201: {"description": "Rol created"},
        401: {"description": "user unauthorized"},
        404: {"description": "rol error"},
    },
)
async def create(new_user: CreateRol):
    rol = await rol_service.create(obj_in=new_user)
    return rol


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Rol update"},
        404: {"description": "rol not found"},
    },
)
async def update(update_user: UpdateRol, id: int = Path(...)):
    await rol_service.update(id=id, obj_in=update_user)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Rol delete"},
        401: {"description": "user unauthorized"},
    },
)
async def delete(id: int = Path(...)):
    rol = await rol_service.delete(id=id)
    if rol == 0:
        raise HTTPException(status_code=404, detail="rol not found")
