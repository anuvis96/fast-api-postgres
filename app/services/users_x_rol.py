from app.infra.postgres.crud.users_x_rol import users_x_rol
from app.infra.services.base_service import BaseService


class UsersXRolService(BaseService):
    async def get_relation_by_user(self, user_id):
        relation_by_user = await self._queries.get_relation_by_user(user_id)
        return relation_by_user

    async def get_relation_by_rol(self, rol_id):
        relation_by_rol= await self._queries.get_relation_by_rol(rol_id)
        return relation_by_rol    

users_x_rol_service = UsersXRolService(crud=users_x_rol)