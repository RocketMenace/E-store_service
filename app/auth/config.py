from app.database.config import GlobalConfig

class AuthConfig(GlobalConfig):
    JWT_ALGORITHM: str
    SECRET_KEY: str
    JWT_EXPIRED: int = 30

auth_config = AuthConfig()