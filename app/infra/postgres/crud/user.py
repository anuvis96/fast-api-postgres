
from typing import Any, Dict, Optional
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.user import User
from app.schemas.user import CreateUser, UpdateUser


class CRUDUser(CRUDBase[User, CreateUser, UpdateUser]):
    async def get_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        user = await self.model.get_or_none(username=username)
        return user


user = CRUDUser(model=User)
