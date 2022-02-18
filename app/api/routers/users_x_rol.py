from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.users_x_rol import (
    CreateUsersXRol,
    UpdateUsersXRol,
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


# @router.get(
#     "/user/{user_id}",
#     response_class=JSONResponse,
#     response_model=List[UserBankGet],
#     status_code=200,
#     responses={
#         200: {"description": "User per banks found"},
#     },
# )
# async def get_bank_user(
#     user_id: int,
# ):
#     user = await user_service.get_byid(id=user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail=f"user {user_id} not found")
#     user_bank = await user_bank_service.get_relation_by_user(user_id=user_id)
#     return user_bank


# @router.get(
#     "/bank/{bank_id}",
#     response_model=List[UserBank],
# )
# async def get_users_bank(
#     bank_id: int,
# ):
#     bank = await bank_service.get_byid(id=bank_id)
#     if bank is None:
#         raise HTTPException(status_code=404, detail=f"bank {bank_id} not found")
#     bank_users = await user_bank_service.get_relation_by_bank(bank_id=bank_id)
#     return bank_users





# @router.post(
#     "/bank/{bank_id}/user/{user_id}",
#     response_class=JSONResponse,
#     status_code=201,
#     responses={
#         201: {"description": "User per bank created"},
#     },
# )
# async def add_user_to_bank(user_id: int, bank_id: int):
#     get_bank = await bank_service.get_byid(id=bank_id)
#     if get_bank is None:
#         raise HTTPException(status_code=404, detail=f"bank {bank_id} not found")
#     get_user = await user_service.get_byid(id=user_id)
#     if get_user is None:
#         raise HTTPException(status_code=404, detail=f"user {user_id} not found")
#     relation = CreateUserBank(user_id=user_id, bank_id=bank_id)
#     await user_bank_service.create(obj_in=relation)
#     bank_new = await user_bank_service.get_relation_by_bank(bank_id=bank_id)
#     return bank_new


# @router.get(
#     "/{id}",
#     response_class=JSONResponse,
#     response_model=UserBank,
#     status_code=200,
#     responses={
#         200: {"description": "User per bank found"},
#         404: {"description": "User per bank not found"},
#     },
# )
# async def by_id(id: int = Path(...)):
#     user_bank = await user_bank_service.get_byid(id=id)
#     if user_bank is None:
#         raise HTTPException(status_code=404, detail="UserBank not found")
#     return user_bank


# @router.patch(
#     "/{id}",
#     response_class=Response,
#     response_model=None,
#     status_code=204,
#     responses={
#         204: {"description": "User per bank update"},
#         404: {"description": "User per bank not found"},
#     },
# )
# async def update(update_user_bank: UpdateUserBank, id: int = Path(...)):
#     await user_bank_service.update(id=id, obj_in=update_user_bank)


# @router.delete(
#     "/{id}",
#     response_class=Response,
#     response_model=None,
#     status_code=204,
#     responses={
#         204: {"description": "User per bank delete"},
#     },
# )
# async def delete(id: int = Path(...)):
#     await user_bank_service.delete(id=id)
