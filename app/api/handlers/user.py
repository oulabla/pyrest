from .. import routes
from aiohttp import web
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func
from aiohttp.web_exceptions import HTTPNotFound, HTTPBadRequest

from sqlalchemy.orm import sessionmaker
from app.db import User, UserSchema
from sqlalchemy.orm import subqueryload


@routes.post('/users')
async def insert_user_action(request):
    async_session = sessionmaker(
        request.app["db"],
        expire_on_commit=False,
        class_=AsyncSession
    )

    req_data = await request.json()
    data = {}
    async with async_session() as session:
        user = User()
        if "name" in req_data.keys():
            name = req_data["name"]
        else:
            raise HTTPBadRequest(text="Field 'name' is required")

        insert_cursor = await session.execute(statement=User.__table__.insert().values(name=name))
        pk = insert_cursor.inserted_primary_key[0]

        query = select(User).where(User.id == pk)
        cursor = await session.execute(query)
        user = cursor.scalars().first()

        user_schema = UserSchema()
        data = user_schema.dump(user)
        await session.commit()

    return web.json_response({
        "success": True,
        "data": data,
    })


@routes.get('/users')
async def get_users_action(request):
    # db = request.app["db"]
    #
    # async_session = sessionmaker(
    #     db, expire_on_commit=False, class_=AsyncSession
    # )

    data = []
    # async with db.connect() as conn:
    #     schema = UserSchema()
    #     query = select(User)
    #     result = await conn.stream(query)
    #     async for row in result:
    #         data.append(schema.dump(row))
    #
    #     await conn.close()



    # async with async_session() as session:
    #     schema = UserSchema()
    #
    #     query = select(func.count(User.id)).select_from(User)
    #     result = await session.execute(query)
    #     count = int(result.scalars().first())
    #
    #     query = select(User)
    #     result = await session.stream(query)
    #     async for row in result.scalars():
    #         row_dump = schema.dump(row)
    #         data.append(row_dump)
    #
    #     await session.commit()
    #
    # await db.dispose()

    total = 0
    data = []
    async with request.app["db"].connect() as conn:
        query = select(func.count("*")).select_from(User)
        cursor = await conn.execute(query)
        total = cursor.scalar()

        user_schema = UserSchema()
        query = select(User)
        cursor = await conn.stream(query)
        async for row in cursor:
            dump = user_schema.dump(row)
            data.append(dump)

    return web.json_response({
        "success": True,
        "total": total,
        "data": data,
    })


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
        query = select(User).options(subqueryload(User.roles)).where(User.id == user_id)
        result = await session.stream(query)
        row = await result.scalars().first()
        if row is None:
            raise HTTPNotFound()

        data = schema.dump(row)

        await session.commit()

    await db.dispose()



    return web.json_response({
        "success": True,
        "data": data,
    })



