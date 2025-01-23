from pydantic import BaseModel, EmailStr, Field


class TokenData(BaseModel):
    type: str
    email: str = Field(alias="sub")
    is_admin: bool


class TokenResponse(BaseModel):
    access_token: str
