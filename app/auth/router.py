from fastapi import APIRouter, status

from app.users.schemas import User, UserIn
from app.users.services import create_user

auth_router = APIRouter()


@auth_router.post(
    path="/register", status_code=status.HTTP_201_CREATED, response_model=User
)
async def register_user(request: UserIn):
    user = await create_user(request)
    return user
