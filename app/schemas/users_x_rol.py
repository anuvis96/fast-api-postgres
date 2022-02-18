from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas.rol import RolInDB
from app.schemas.user import UserInDB

class BaseUsersXRol(BaseModel):
    user: int
    rol: int

class CreateUsersXRol(BaseUsersXRol):
    pass

class UpdateUsersXRol(BaseModel):
    pass

class PayloadUsersXRol(BaseModel):
    user: Optional[int]
    rol: Optional[int]
   


class UsersXRolInDB(BaseUsersXRol):
    id: int
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True


class UsersXRolResponse(BaseModel):
    id: int
    user: Optional[UserInDB]
    rol: Optional[RolInDB]
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True