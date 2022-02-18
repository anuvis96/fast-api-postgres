from tortoise import fields, Model



class UsersxRol(Model):
    user = fields.ForeignKeyField(
        "models.User", related_name="user"
    )
    rol = fields.ForeignKeyField(
        "models.Rol", related_name="rol"
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)