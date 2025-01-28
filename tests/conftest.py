import pytest
from app.database.config import config
from typing import AsyncGenerator

from app.database.services import fill_roles_table, create_admin
from app.database.settings import database
from fastapi.testclient import TestClient
from app.main import app
from httpx import AsyncClient, ASGITransport


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture()
def client():
    yield TestClient(app)


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    await database.connect()
    await fill_roles_table()
    await create_admin()
    yield
    await database.disconnect()




# @pytest.fixture()
# async def async_client(client):
#     async with AsyncClient(appbase_url=client.base_url) as ac:
#         yield ac

@pytest.fixture()
async def registered_user_token():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = ac.post("/auth/login", json={"email": "bob_6@example.com", "password": "String123$"})
    return response