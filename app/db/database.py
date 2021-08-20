from sqlalchemy.ext.asyncio import create_async_engine

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:U5w6yZvpBNAjcSLZZx2jb5nfuySa6ZQF@postgresql.oknago-dev.svc/alchemy?serverVersion=9.6.9"

database = create_async_engine(
    "postgresql+asyncpg://postgres:U5w6yZvpBNAjcSLZZx2jb5nfuySa6ZQF@92.63.110.64/alchemy",
    echo=True,
)



