from typing import Annotated

from fastapi import Depends

from app.database.settings import SessionLocal


async def get_session():
    async with SessionLocal() as session:
        yield session


SessionDep = Annotated[SessionLocal, Depends(get_session)]
