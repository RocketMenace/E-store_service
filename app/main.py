from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.settings import database
from app.auth.router import auth_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan, root_path="/api/v1")

app.include_router(auth_router, prefix="/auth", tags=["auth"])