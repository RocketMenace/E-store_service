from sqlalchemy import Insert

from app.database.settings import engine


async def execute(query: Insert) -> None:
    async with engine as conn:
        await conn.execute(query)
