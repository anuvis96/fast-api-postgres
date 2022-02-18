from typing import Union, List

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.users_x_rol import UsersxRol
from app.schemas.users_x_rol import CreateUsersXRol, UpdateUsersXRol

class CRUDUsersXRol(
    CRUDBase[UsersxRol, CreateUsersXRol, UpdateUsersXRol]
):
  async def get_relation_by_user(self, user_id: int):
        obj_user_id = await self.model.filter(user_id=user_id).prefetch_related(
            "rol", "user"
        )
        if obj_user_id is None:
            return None
        return obj_user_id


users_x_rol = CRUDUsersXRol(model=UsersxRol)