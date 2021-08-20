from sqlalchemy import Column, DateTime, String, Integer, Table, ForeignKey, func
from sqlalchemy.orm import relationship

from .. import Base


roles_assoc_table = Table(
    'users_roles',
    Base.metadata,
    Column('user_id', ForeignKey("users.id"), primary_key=True),
    Column('role_id', ForeignKey("roles.id"), primary_key=True),
)


class User(Base):
    __tablename__ = 'users'
    __jsonexport__ = ['id', 'name', 'created_at'],
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())
    roles = relationship("Role", secondary=roles_assoc_table)
