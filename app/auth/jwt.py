from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import Depends

from app.auth.config import auth_config
from app.users.schemas import AuthUser
from app.auth.exceptions import InvalidToken
from app.auth.schemas import TokenData
from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = auth_config.SECRET_KEY
ALGORITHM = auth_config.JWT_ALGORITHM
JWT_EXPIRED = auth_config.JWT_EXPIRED


def create_access_token(request: AuthUser):
    expire_delta = timedelta(minutes=JWT_EXPIRED)
    jwt_data = {
        "sub": request.email,
        "exp": datetime.now(tz=timezone.utc) + expire_delta,
        "is_admin": request.is_admin
    }
    return jwt.encode(jwt_data, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    if not token:
        return None
    try:
        payload = jwt.decode(token, auth_config.SECRET_KEY, algorithms=auth_config.JWT_ALGORITHM)
    except jwt.PyJWTError:
        raise InvalidToken()
    return TokenData(**payload)