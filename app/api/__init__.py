from aiohttp import web

routes = web.RouteTableDef()

from .views import *
from .server import Server


