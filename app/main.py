from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.auth.router import auth_router
from app.database.services import create_admin, fill_roles_table
from app.database.settings import database, engine, metadata
from app.products.router import products_router
from app.users.router import users_router
from app.shopping_cart.router import shopping_cart_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    metadata.create_all(engine)
    await database.connect()
    await fill_roles_table()
    await create_admin()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan, root_path="/api/v1")

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(shopping_cart_router, prefix="/shopping", tags=["shopping"])
