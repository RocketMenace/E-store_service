import pytest
from httpx import ASGITransport, AsyncClient

from tests.conftest import app


@pytest.mark.anyio
async def test_register_user():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.post(
            "/users/register",
            json={
                "first_name": "Bob",
                "last_name": "Black",
                "middle_name": "Martin",
                "email": "bob_6@example.com",
                "phone": "+78530457969",
                "password": "String123$",
                "password_repeat": "String123$",
            },
        )
    assert response.status_code == 201
    assert response.json() == {
        "first_name": "Bob",
        "last_name": "Black",
        "middle_name": "Martin",
        "email": "bob_6@example.com",
        "phone": "+78530457969",
        "id": 2,
    }
