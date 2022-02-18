from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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

class UserInDB(BaseUser):
    id: int
    created_at: Optional[datetime]
    last_modified: Optional[datetime]

    class Config:
        orm_mode = True    #Activa el schemma para que tortoise lo reconozca
 