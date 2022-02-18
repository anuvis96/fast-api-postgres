from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.rol import Rol
from app.schemas.rol import CreateRol, UpdateRol


class CRUDRol(CRUDBase[Rol, CreateRol, UpdateRol]):
    ...


rol = CRUDRol(Rol)
