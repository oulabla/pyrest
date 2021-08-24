from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models import Role


class RoleSchema(SQLAlchemySchema):
    class Meta:
        model = Role
        load_instance = True
        # transient = True

    id = auto_field()
    name = auto_field()
