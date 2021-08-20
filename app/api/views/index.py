from aiohttp import web
from .. import routes


@routes.view('/')
class IndexView(web.View):

    async def get(self):
        return web.Response(text="asd")