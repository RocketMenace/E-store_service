import pytest
from app.database.config import config
from typing import AsyncGenerator

from app.database.services import fill_roles_table, create_admin
from app.database.settings import database
from fastapi.testclient import TestClient
from app.main import app
from httpx import AsyncClient


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


@pytest.fixture()
async def registered_user(): ...


@pytest.fixture()
async def async_client(client):
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
