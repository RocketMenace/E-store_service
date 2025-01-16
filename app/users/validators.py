import re
from typing import Annotated

from pydantic import AfterValidator


def phone_number_validator(phone: str) -> str:
    phone_pattern = re.compile(r"^\+7\d{10}$")
    if not phone_pattern.match(phone):
        raise ValueError(
            "Номер телефона должен быть длиной в десять символов и начинаться с '+7'"
        )
    return phone


def password_pattern_validator(password: str) -> str:
    password_pattern = re.compile(r"^(?=.*\d)(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$")
    if not re.match(password_pattern, password):
        raise ValueError(
            "Пароль должен содержать"
            "не менее 8 символов"
            "только латинcкие буквы"
            "минимум 1 символ верхнего регистра"
            "минимум 1 спец символ '$%&!:'"
        )
    return password


CheckPhone = Annotated[str, AfterValidator(phone_number_validator)]
CheckPasswordPattern = Annotated[str, AfterValidator(password_pattern_validator)]
