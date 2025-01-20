from typing import Any

from app.auth.security import hash_password
from app.database.settings import database
from app.users.models import users_table
from app.users.schemas import UserIn


async def create_user(request: UserIn) -> dict[str, Any] | None:
    query = (
        users_table.insert()
        .values(
            {
                "first_name": request.first_name,
                "last_name": request.last_name,
                "middle_name": request.middle_name,
                "email": request.email,
                "phone": request.phone,
                "password": hash_password(request.password),
                # "is_admin": request.is_admin,
            }
        )
        .returning(users_table)
    )
    return await database.fetch_one(query)
