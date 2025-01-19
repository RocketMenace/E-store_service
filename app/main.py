from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.users.router import users_router
from app.auth.router import auth_router
from app.products.router import products_router
from app.database.settings import database, engine, metadata


@asynccontextmanager
async def lifespan(application: FastAPI):
    metadata.create_all(engine)
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan, root_path="/api/v1")

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(products_router, prefix="/products", tags=["products"])
