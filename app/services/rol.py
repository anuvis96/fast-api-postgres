#from datetime import datetime

from app.infra.postgres.crud.rol import rol
from app.infra.services.base_service import BaseService


class RolService(BaseService):
   ...    


rol_service = RolService(crud=rol)