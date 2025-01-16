from typing import Any

from pydantic import EmailStr

from app.database.settings import database
from app.users.models import users_table
from app.users.schemas import AuthUser
from app.auth.exceptions import InvalidCredentials
from app.auth.security import check_password


async def get_user_by_email(email: EmailStr) -> dict[str, Any] | None:
    query = users_table.select().where(users_table.c.email == email)
    result = await database.fetch_one(query)
    if result:
        return result

async def authenticate_user(request: AuthUser) -> dict[str, Any]:
    user = await get_user_by_email(request.email)
    if not user:
        raise InvalidCredentials()
    if not check_password(user["password"], request.password):
        raise InvalidCredentials()
    return user

async def get_current_user():
    pass
