from pydantic import BaseModel, EmailStr

class TokenData(BaseModel):
    email: EmailStr
    is_admin: bool

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
