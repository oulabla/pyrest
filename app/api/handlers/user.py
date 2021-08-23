from .. import routes
from aiohttp import web
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from aiohttp.web_exceptions import HTTPNotFound

from sqlalchemy.orm import sessionmaker
from app.db import User, UserSchema


@routes.get('/users')
async def get_users_action(request):
    db = request.app["db"]

    async_session = sessionmaker(
        db, expire_on_commit=False, class_=AsyncSession
    )

    data = []
    async with async_session() as session:
        schema = UserSchema()
        query = select(User)
        result = await session.execute(query)
        for row in result.scalars():
            data.append(schema.dump(row))

        await session.commit()

    await db.dispose()

    return web.json_response(data)


@routes.get('/users/{id}')
async def get_user_action(request):
    db = request.app["db"]

    async_session = sessionmaker(
        db, expire_on_commit=False, class_=AsyncSession
    )

    user_id = int(request.match_info['id'])

    data = {}
    async with async_session() as session:
        schema = UserSchema()
        query = select(User).where(User.id == user_id)
        result = await session.stream(query)
        row = await result.scalars().first()
        if row is None:
            raise HTTPNotFound()

        data = schema.dump(row)

        await session.commit()

    await db.dispose()

    return web.json_response(data)



