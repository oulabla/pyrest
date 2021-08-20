from aiohttp import web
from app.db.database import database

Db = database
routes = web.RouteTableDef()


from .views import *
from .server import Server


