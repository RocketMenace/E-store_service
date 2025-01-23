from typing import Any, Annotated

from pydantic import EmailStr

from app.auth.exceptions import InvalidCredentials
from app.auth.security import check_password
from app.database.settings import database
from app.users.models import users_table
from app.users.schemas import AuthUser, User


def check_user_is_admin(user: dict[str, Any]) -> bool:
    if user["role"] == 1:
        return True
    return False


async def get_user_by_email(email: str) -> User | None:
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


# async def get_current_user(token: Annotated[]):
#     pass
