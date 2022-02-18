from typing import TYPE_CHECKING, TypeVar

from pydantic import BaseModel, Field
from tortoise.models import Model

if TYPE_CHECKING:
    from app.infra.postgres.crud.base import CRUDBase


ModelType = TypeVar("ModelType", bound=Model)

CrudType = TypeVar("CrudType", bound="CRUDBase")

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CountDB(BaseModel):
    count: int = Field(...)
