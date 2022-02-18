from tortoise import fields, Model


class Rol(Model):
    name = fields.CharField(unique=True, max_length=255)
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)
