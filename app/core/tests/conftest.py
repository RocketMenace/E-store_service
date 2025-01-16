from typing import Generator, AsyncGenerator
from fastapi.testclient import TestClient

import pytest
from httpx import AsyncClient

from app.database.settings import database
from app.main import app
from app.users.models import users_table
from app.auth.models import tokens

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)

@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    users_table.clear()
    tokens.clear()
    await database.connect()
    yield
    await database.disconnect()

@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app, base_url=client) as ac:
