from fastapi import APIRouter, status

from app.auth.dependencies import CheckEmail
from app.shopping_cart.services import create_shopping_cart
from app.users.schemas import User
from app.users.services import create_user

users_router = APIRouter()


@users_router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
    summary="Add user to database.",
    response_description="On successful registration, the API will respond with a 201 Created status code and the details of the registered user in JSON format.",
)
async def register_user(request: CheckEmail):
    """
    This endpoint allows users to create an account in the database.
    The user's credential must be provided in the request body.
    Upon successful registration, the endpoint returns the details of the newly registered user.
    - **first_name**
    - **last_name**
    - **middle_name**
    - **email**
    - **phone** The phone number must be ten characters long and start with '+7'
    - **password** The password must contain
            at least 8 characters,
            Latin letters only,
            at least 1 upper case character,
            at least 1 special character $%&!
    - **password_repeat**
    """
    user = await create_user(request)
    await create_shopping_cart(user["id"])  # Need transaction !?
    return user
