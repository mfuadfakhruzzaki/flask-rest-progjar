# app/schemas/user.py
from ..extensions import ma
from ..models.user import User
from marshmallow import fields, validate

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        # Hapus exclude karena kita akan mengatur password secara eksplisit

    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6))
