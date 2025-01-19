from app.auth.constants import ErrorCode
from app.core.exceptions import BadRequest, NotAuthenticated
from jwt import ExpiredSignatureError
from fastapi import status


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS

class TokenExpired(NotAuthenticated):
    DETAIL = ErrorCode.TOKEN_EXPIRED

class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN

   

