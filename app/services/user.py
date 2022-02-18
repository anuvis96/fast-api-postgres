#from datetime import datetime

from app.infra.postgres.crud.user import user
from app.infra.services.base_service import BaseService


class UserService(BaseService):
    async def get_by_username(self, username: str):
        user = await self._queries.get_by_username(username=username)
        return user     


user_service = UserService(crud=user)
