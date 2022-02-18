from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseRol(BaseModel):
    name: str
    description: str

class PayloadRol(BaseModel):
    name: Optional[str]
    description: Optional[str]

class CreateRol(BaseRol):
    pass

class UpdateRol(PayloadRol):
    pass

class RolInDB(BaseRol):
    id: int
    created_at: Optional[datetime]
    last_modified: Optional[datetime]

    class Config:
        orm_mode = True