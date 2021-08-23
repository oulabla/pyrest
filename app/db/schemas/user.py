from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow.fields import Date, DateTime, Time
from ..models import User


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field()
    name = auto_field()
    created_at = Date()
