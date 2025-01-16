from datetime import timedelta, datetime, timezone
from app.auth.config import auth_config
from app.users.schemas import AuthUser
import jwt


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

