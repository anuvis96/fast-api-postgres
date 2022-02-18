from tortoise import fields, Model


class User(Model):
    name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=200)
    email = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=255, null=True)
    username = fields.CharField(unique=True, max_length=255)
    password = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)
    

    

   