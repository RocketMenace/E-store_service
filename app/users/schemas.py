from re import compile

from pydantic import BaseModel, EmailStr, Field, model_validator

from app.users.validators import CheckPhone


class UserBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: EmailStr
    phone: CheckPhone


class UserIn(UserBase):
    password: str
    password_repeat: str
    is_admin: bool = Field(default=False)

    @model_validator(mode="after")
    def valid_password(self) -> str:
        password_pattern = compile(
            r"^(?=.*[A-Z])(?=.*[$%&!:])(?=[a-zA-Z]*$)(?=.{8,}).*$"
        )
        if not password_pattern.match(self.password):
            raise ValueError(
                "Пароль должен содержать"
                "не менее 8 символов"
                "только латинcкие буквы"
                "минимум 1 символ верхнего регистра"
                "минимум 1 спец символ '$%&!:'"
            )
        if self.password != self.password_repeat:
            raise ValueError("Пароли не совпадают.")
        return self.password


class User(UserBase):
    id: int
