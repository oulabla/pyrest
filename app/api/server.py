from aiohttp import web
from . import routes
from sqlalchemy import engine
from asyncpgsa import pg
# from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import create_async_engine

class Server:

    def __init__(self):
        self.app = web.Application()
        print(routes)
        self.app.add_routes(routes)

        # self.app.on_startup.append(self.init_pg)
        self.app.cleanup_ctx.append(Server.init_pg)

    @staticmethod
    async def close_pg(app):
        app["db"].close()

    @staticmethod
    async def init_pg(app):
        db = create_async_engine(
            "postgresql+asyncpg://postgres:U5w6yZvpBNAjcSLZZx2jb5nfuySa6ZQF@92.63.110.64/alchemy",
            echo=True,
        )
        app["db"] = db
        yield
        db.close()
        await db.wait_closed()
        print("waited")

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