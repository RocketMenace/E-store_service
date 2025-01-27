from pytest import raises

from app.users.validators import phone_number_validator


def test_phone_number_validation():
    correct_number = "+78888888888"
    incorrect_number = "45651"
    assert correct_number == phone_number_validator("+78888888888")
    with raises(ValueError):
        phone_number_validator(incorrect_number)
