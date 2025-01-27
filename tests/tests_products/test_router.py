import pytest
from httpx import ASGITransport, AsyncClient

from tests.conftest import app


@pytest.mark.anyio
async def test_get_products_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.get("/products")
    assert response.status_code == 401


# @pytest.mark.anyio
# async def test_get_products():
#     async with AsyncClient(
#         transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
#     ) as ac:
#         response = await ac.get("/products", headers={""})


@pytest.mark.anyio
async def test_add_product_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.post(
            "/products/create", json={"name": "flower", "price": 100, "is_active": True}
        )

    assert response.status_code == 401

@pytest.mark.anyio
async def test_update_product_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.put(
            "/products/update/1", json={"name": "flower", "price": 100, "is_active": True}
        )
    assert response.status_code == 401

@pytest.mark.anyio
async def test_update_product_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/api/v1"
    ) as ac:
        response = await ac.delete(
            "/products/delete/1"
        )
    assert response.status_code == 401
