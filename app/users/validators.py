from re import compile
from typing import Annotated

from pydantic import AfterValidator


def phone_number_validator(phone: str) -> str:
    phone_pattern = compile(r"^\+7\d{10}$")
    if not phone_pattern.match(phone):
        raise ValueError(
            "Номер телефона должен быть длиной в десять символов и начинаться с '+7'"
        )
    return phone


CheckPhone = Annotated[str, AfterValidator(phone_number_validator)]
