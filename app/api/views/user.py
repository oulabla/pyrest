from aiohttp import web
from .. import routes

@routes.view('/users')
class UserView(web.View):

    async def get(self):
        data = {
            "id" : 10,
        }
        return web.json_response(data)