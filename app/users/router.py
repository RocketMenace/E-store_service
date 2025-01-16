from fastapi import APIRouter, status

from app.auth.dependencies import CheckEmail
from app.users.schemas import User
from app.users.services import create_user

users_router = APIRouter()


@users_router.post(
    path="/register", status_code=status.HTTP_201_CREATED, response_model=User
)
async def register_user(request: CheckEmail):
    user = await create_user(request)
    return user