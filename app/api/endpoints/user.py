#from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import JSONResponse
from app.utils.encript import pwd_encrip

from app.schemas.user import (
    AuthUser,
    UserInDB,
    CreateUser,
    PayloadUser,
    UserResponse,
)

from app.services.user import user_service


router = APIRouter()

@router.post(
    "",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=201,
    responses={
        201: {"description": "user created"},
    },
)
async def create(new_user: CreateUser):
    user = await user_service.get_by_username(username=new_user.username)
    if user is not None:
        raise HTTPException(status_code=400, detail="user already exists in database")
    password = pwd_encrip(new_user.password)
    new_user.password = password
    user = await user_service.create(obj_in=new_user)
    return user


@router.post(
    "/auth/",
    response_class=JSONResponse,
    response_model=UserResponse,
    status_code=200,
    responses={
        200: {"description": "users found"},
        401: {"description": "User unauthorized"},
    },
)
async def auth_user(*, user_in: AuthUser):
    users = await user_service.auth_user(user=user_in)
    if users:
        return users
    return []


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


