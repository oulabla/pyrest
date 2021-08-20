from aiohttp import web
from . import routes
from sqlalchemy import engine
from asyncpgsa import pg
from sqlalchemy.ext.asyncio import create_async_engine


class Server:

    def __init__(self):
        self.app = web.Application()
        self.app.add_routes(routes)

        # self.app.on_startup.append(self.init_pg)

    @staticmethod
    async def init_pg(self):
        pass

        # await pg.init(
        #     host='92.63.110.64',
        #     database='alchemy',
        #     user='postgres',
        #     # loop=loop,
        #     password='U5w6yZvpBNAjcSLZZx2jb5nfuySa6ZQF',
        #     min_size=5,
        #     max_size=10
        # )

    def run(self):
        web.run_app(self.app)