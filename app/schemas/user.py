from datetime import datetime
from lib2to3.pgen2.token import OP
from typing import Optional

from pydantic import BaseModel

from app.schemas.users_x_rol import UsersXRolInDB
from app.schemas.rol import RolInDB


class BaseUser(BaseModel):
    name: str
    last_name: str
    phone: Optional[str]
    username: Optional[str]
    password: Optional[str]

class AuthUser(BaseModel):
    username: Optional[str]
    password: Optional[str]

class PayloadUser(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    username: Optional[str]

class UserResponse(BaseModel):
    id: Optional[int]
    name: str
    last_name: str
    phone: Optional[str]
    username: Optional[str]
    created_at: Optional[datetime]
    last_modified: Optional[datetime]

    class Config:
        orm_mode = True


class CreateUser(BaseUser):
    pass

class UpdateUser(PayloadUser):
    pass

class UserComplete(BaseUser):
    id: Optional[int]
    rol: Optional[RolInDB]
    users_x_rol: Optional[UsersXRolInDB]
    created_at: Optional[datetime]
    last_modified: Optional[datetime]

    class Config:
        orm_mode = True
    
class UserInDB(BaseUser):
    id: int
    created_at: Optional[datetime]
    last_modified: Optional[datetime]

    class Config:
        orm_mode = True    #Activa el schemma para que tortoise lo reconozca
 