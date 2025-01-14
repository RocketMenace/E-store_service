from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.auth.router import auth_router
from app.database.settings import database, engine, metadata


@asynccontextmanager
async def lifespan(application: FastAPI):
    metadata.create_all(engine)
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan, root_path="/api/v1")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
