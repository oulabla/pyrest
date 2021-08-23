import time

from aiohttp import web
from sqlalchemy.ext.asyncio import AsyncSession

from .. import routes
from asyncpgsa import PG

from app.db import User
from .. import Db
from app.db import Base, User, UserSchema
import json
from sqlalchemy.ext.serializer import dumps, loads


from aiohttp.web_urldispatcher import View

@routes.view('/users')
class UserView(View):

    async def get(self, request):

        # user = User()
        # user.name = "lala"
        #
        # user_schema = UserSchema();


        # user.created_at = time.time()


        # async with AsyncSession(Db) as session:
        #     async with session.begin():
        #
        #
        #         session.add_all(
        #             [
        #                 user
        #             ]
        #         )
        #         await session.commit()
        # print(json.dumps(user))
        # loads(user, Base.metadata)

        return web.json_response({})