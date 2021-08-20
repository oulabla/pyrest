import time

from aiohttp import web
from sqlalchemy.ext.asyncio import AsyncSession

from .. import routes
from asyncpgsa import PG

from app.db import User
from .. import Db
from app.db import Base, User
import json
from sqlalchemy.ext.serializer import dumps, loads

class Encoder(json.JSONEncoder):
    def default(self, obj) :
        if isinstance(obj, Base):
            return dict(zip(obj.__jsonexport__, [getattr(obj, v) for v in obj.__jsonexport__]))
        return json.JSONEncoder.default(self, obj)

@routes.view('/users')
class UserView(web.View):

    async def get(self):
        user = User()
        user.name = "lala"
        # user.created_at = time.time()


        async with AsyncSession(Db) as session:
            async with session.begin():


                session.add_all(
                    [
                        user
                    ]
                )
                await session.commit()

        loads(user, Base.metadata)

        return web.json_response({})