from fastapi import APIRouter, status

from app.auth.jwt import create_access_token
from app.auth.schemas import TokenResponse
from app.auth.services import authenticate_user
from app.users.schemas import AuthUser

auth_router = APIRouter()


@auth_router.post(
    path="/login", status_code=status.HTTP_200_OK, response_model=TokenResponse
)
async def login(request: AuthUser):
    user = await authenticate_user(request)
    access_token = create_access_token(user)
    return TokenResponse(access_token=access_token)
