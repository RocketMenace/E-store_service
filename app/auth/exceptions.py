from fastapi import status
from jwt import ExpiredSignatureError

from app.auth.constants import ErrorCode
from app.core.exceptions import BadRequest, NotAuthenticated


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class TokenExpired(NotAuthenticated):
    DETAIL = ErrorCode.TOKEN_EXPIRED


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN


class AuthRequired(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class AuthorizationFailed(NotAuthenticated):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED
