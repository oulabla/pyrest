from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow.fields import Date
from marshmallow_sqlalchemy.fields import Nested

from ..models import User
from .role import RoleSchema


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field()
    name = auto_field()
    created_at = Date()

    roles = Nested(RoleSchema, many=True)
