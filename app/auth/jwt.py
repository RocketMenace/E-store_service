from datetime import datetime, timedelta, timezone
from typing import Annotated, Any

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.auth.config import auth_config
from app.auth.exceptions import AuthorizationFailed, AuthRequired, InvalidToken
from app.auth.schemas import TokenData
from app.auth.services import check_user_is_admin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = auth_config.SECRET_KEY
ALGORITHM = auth_config.JWT_ALGORITHM
JWT_EXPIRED = auth_config.JWT_EXPIRED


def create_access_token(user: dict[str, Any]):
    expire_delta = timedelta(minutes=JWT_EXPIRED)
    jwt_data = {
        "sub": user["email"],
        "exp": datetime.now(tz=timezone.utc) + expire_delta,
        "is_admin": check_user_is_admin(user),
    }
    return jwt.encode(jwt_data, key=SECRET_KEY, algorithm=ALGORITHM)


async def decode_token(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> TokenData | None:
    if not token:
        return None
    try:
        payload = jwt.decode(
            token, auth_config.SECRET_KEY, algorithms=auth_config.JWT_ALGORITHM
        )
    except jwt.PyJWTError:
        raise InvalidToken()
    return TokenData(**payload, type="bearer")


async def check_user_jwt(token: Annotated[TokenData | None, Depends(decode_token)]):
    if not token:
        raise AuthRequired()
    return token


async def check_is_admin(token: Annotated[TokenData, Depends(check_user_jwt)]):
    if not token.is_admin:
        raise AuthorizationFailed()
    return token


async def check_admin_access(token: Annotated[TokenData, Depends(check_is_admin)]):
    if token and token.is_admin:
        return
    raise AuthorizationFailed()
