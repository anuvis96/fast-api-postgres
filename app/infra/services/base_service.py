from typing import Any, Dict, List, Optional, Union

from app.infra.services.base import IServiceBase
from app.schemas.general import CreateSchemaType, CrudType, ModelType, UpdateSchemaType


class BaseService(IServiceBase[CreateSchemaType, UpdateSchemaType]):
    def __init__(self, crud: CrudType):
        self._queries = crud

    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        new_obj = await self._queries.create(obj_in=obj_in)
        return new_obj

    async def get_byid(self, *, id: Union[int, str]) -> Optional[ModelType]:
        obj_found = await self._queries.get_byid(id=id)
        if obj_found:
            return obj_found
        return None

    async def get_all(
        self,
        *,
        payload: Optional[Dict[str, Any]],
        skip: int,
        limit: int,
    ) -> List[ModelType]:
        objs_found = await self._queries.get_all(
            payload=payload,
            skip=skip,
            limit=limit,
        )
        return objs_found

    async def update(self, *, id: Union[int, str], obj_in: UpdateSchemaType) -> bool:
        payload = obj_in.dict(exclude_unset=True)
        obj_updated = await self._queries.update(id=id, obj_in=payload)
        return obj_updated

    async def delete(self, *, id: Union[int, str]) -> int:
        obj_removed = await self._queries.delete(id=id)
        return obj_removed

    async def count(self, *, payload: Dict[str, Any] = {}) -> int:
        count = await self._queries.count(payload=payload)
        return count
