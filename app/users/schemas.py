from pydantic import BaseModel, Field, field_validator, EmailStr
from app.users.validators import CheckPhone
from re import compile


class UserBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: EmailStr
    phone: CheckPhone


class UserIn(UserBase):
    password: str
    password_repeat: str

    @field_validator("password", "password_repeat", mode="after")
    def valid_password(self) -> str:
        password_pattern = compile(
            r"^(?=.*[A-Z])(?=.*[$%&!:])(?=[a-zA-Z]*$)(?=.{8,}).*$"
        )
        if not password_pattern.match(self.password):
            raise ValueError(
                "Пароль должен содержать"
                "не менее 8 символов"
                "только латиница"
                "минимум 1 символ верхнего регистра"
                "минимум 1 спец символ '$%&!:'"
            )
        if self.password != self.password_repeat:
            raise ValueError("Пароли не совпадают.")
        return self.password


class User(UserBase):
    id: int
