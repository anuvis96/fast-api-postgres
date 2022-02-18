from typing import Union, List

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.users_x_rol import UsersxRol
from app.schemas.users_x_rol import CreateUsersXRol, UpdateUsersXRol

class CRUDUsersXRol(
    CRUDBase[UsersxRol, CreateUsersXRol, UpdateUsersXRol]
):
    async def create(self, *, obj_in: CreateUsersXRol) -> Union[dict, None]:
        user_data = obj_in.dict()
        users_x_rol = await self.model.create(
            user_id=obj_in.user_,
            rol_id=obj_in.rol_,
            **user_data,
        )
        return users_x_rol


    async def get_all(
        self,
        *,
        payload: dict = None,
        skip: int = 0,
        limit: int = 10,
    ) -> List:
        if payload:
            model = (
                await self.model.filter(**payload)
                .offset(skip)
                .limit(limit)
                .all()
                .prefetch_related("user", "rol")
            )
        else:
            model = await self.model.all().prefetch_related("user", "rol")
        return model
    
users_x_rol = CRUDUsersXRol(UsersxRol)


