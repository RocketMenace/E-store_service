from typing import Any

from sqlalchemy import insert

from app.auth.security import hash_password
from app.users.models import users_table
from app.users.schemas import UserIn

async  def create_user(request: UserIn) ->  dict[str, Any] | None:
    query = insert(users_table).values(
        {
            "first_name": request.first_name,
            "last_name": request.last_name,
            "middle_name": request.middle_name,
            "email": request.email,
            "phone": request.phone,
            "password": hash_password(request.password)
        }
    ).returning(users_table)
    return await ...