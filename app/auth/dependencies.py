from typing import Annotated

from fastapi import Depends

from app.auth.exceptions import EmailTaken
from app.auth.services import get_user_by_email
from app.users.schemas import UserIn


async def is_email_taken(request: UserIn) -> UserIn:
    if await get_user_by_email(request.email):
        raise EmailTaken()
    return request


CheckEmail = Annotated[UserIn, Depends(is_email_taken)]
