
from typing import Union
from typing import Any, Dict, Optional
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.user import User
from app.schemas.user import AuthUser, CreateUser, UpdateUser


class CRUDUser(CRUDBase[User, CreateUser, UpdateUser]):
    async def auth_user(self, *, user: AuthUser) -> Union[dict, None]:
        model = await self.model.filter(username=user.username).all()
        if model:
            return model[0] if model[0].password == user.password else None
        return None

    async def get_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        user = await self.model.get_or_none(username=username)
        return user


user = CRUDUser(User)
