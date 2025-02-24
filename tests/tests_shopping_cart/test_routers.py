import pytest
from httpx import ASGITransport, AsyncClient

from tests.conftest import app

@pytest.mark.anyio
async def test_add_product_to_cart_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.post("/shopping/add_product?product_id=2&quantity=1")
    assert response.status_code == 401

@pytest.mark.anyio
async def test_add_product_to_cart_with_admin_permissions():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        user_token = user_token = await ac.post("/auth/login", json={"email": "bob_6@example.com", "password": "String123$"})
        response = await ac.post("/shopping/add_product?product_id=2&quantity=1", headers={"Authorization": "Bearer " + user_token.json()["access_token"]})
    assert response.status_code == 200

@pytest.mark.anyio
async def test_cart_remove_product_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.delete("/shopping/remove_product?product_id=2")
    assert response.status_code == 401

@pytest.mark.anyio
async def test_cart_clear_products_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.delete("/shopping/clear_cart")
    assert response.status_code == 401