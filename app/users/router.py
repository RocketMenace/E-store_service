from fastapi import APIRouter, status

from app.auth.dependencies import CheckEmail
from app.users.schemas import User
from app.users.services import create_user
from app.shopping_cart.services import create_shopping_cart

users_router = APIRouter()


@users_router.post(
    path="/register", status_code=status.HTTP_201_CREATED, response_model=User
)
async def register_user(request: CheckEmail):
    user = await create_user(request)
    await create_shopping_cart(user["id"])  # Need transaction !?
    return user
