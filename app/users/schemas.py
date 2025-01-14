from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator

from app.users.validators import CheckPasswordPattern, CheckPhone


class UserBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: EmailStr
    phone: CheckPhone


class UserIn(UserBase):
    password: CheckPasswordPattern
    password_repeat: str
    is_admin: bool = Field(default=False)

    @model_validator(mode="after")
    def check_password_match(self):
        if self.password != self.password_repeat:
            raise ValueError("Пароли не совпадают!")
        return self


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
