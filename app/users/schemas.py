from pydantic import BaseModel, ConfigDict, model_validator

from app.users.validators import CheckPasswordPattern, CheckPhone


class UserBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: str
    phone: CheckPhone


class AuthUser(BaseModel):
    email: str
    password: str


class UserIn(UserBase):
    password: CheckPasswordPattern
    password_repeat: str
    # is_admin: bool

    @model_validator(mode="after")
    def check_password_match(self):
        if self.password != self.password_repeat:
            raise ValueError("Пароли не совпадают!")
        return self


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
