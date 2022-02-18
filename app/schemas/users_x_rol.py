from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class UsersXRolBase(BaseModel):
    user_id: int
    rol_id: int

class CreateUsersXRol(UsersXRolBase):
    pass

class UpdateUsersXRol(BaseModel):
    user_id: Optional[int]
    rol_id: Optional[int]

class SearchUsersXRol(UpdateUsersXRol):
    pass

class UsersXRolInDB(UsersXRolBase):
    id: int
    created_at: datetime
    last_modified: datetime   

class UsersXRol(UsersXRolInDB):
    class Config:
        orm_mode = True
