from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, Union

from app.schemas.general import CreateSchemaType, CrudType, ModelType, UpdateSchemaType


class IServiceBase(Generic[CreateSchemaType, UpdateSchemaType], ABC):  # type: ignore
    @abstractmethod
    def __init__(self, crud: CrudType):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        raise NotImplementedError

    @abstractmethod
    async def get_byid(self, *, id: Union[int, str]) -> Optional[ModelType]:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self,
        *,
        payload: Optional[Dict[str, Any]],
        skip: int,
        limit: int,
    ) -> List[ModelType]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *, id: Union[int, str], obj_in: UpdateSchemaType) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, id: Union[int, str]) -> int:
        raise NotImplementedError

    @abstractmethod
    async def count(self, *, payload: Optional[Dict[str, Any]]) -> int:
        raise NotImplementedError
