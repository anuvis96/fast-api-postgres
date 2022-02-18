#from datetime import datetime
from typing import List, TypeVar, Optional, Dict, Any

from app.crud.base import ICrudBase
from app.infra.postgres.crud.user import user
from app.infra.services.base_service import BaseService

QueryType = TypeVar("QueryType", bound=ICrudBase)


class UserService(BaseService):
    # def __init__(self, user_queries: QueryType):
    #     self.__user_queries = user_queries

    # async def get_all(
    #     self,
    #     *,
    #     payload: Optional[Dict[str, Any]],
    #     skip: int,
    #     limit: int,
    # ):
    #     objs_found = await self.__user_queries.get_all(
    #         payload=payload,
    #         skip=skip,
    #         limit=limit,
    #     )
    #     return objs_found

    async def get_by_username(self, username: str):
        user = await self._queries.get_by_username(username=username)
        return user     


user_service = UserService(crud=user)
