from datetime import datetime, timezone
from typing import Any

from app.database.settings import database
from app.products.models import products_table
from app.products.schemas import ProductIn


async def create_product(request: ProductIn) -> dict[str, Any]:
    query = (
        products_table.insert()
        .values(
            {
                "name": request.name,
                "price": request.price,
                "is_active": request.is_active,
            }
        )
        .returning(products_table)
    )
    return await database.fetch_one(query)


async def remove_product(product_id: int):
    query = products_table.delete().where(products_table.c.id == product_id)
    await database.execute(query)


async def edit_product(product_id: int, request: ProductIn):
    query = (
        products_table.update()
        .where(products_table.c.id == product_id)
        .values(
            {
                "name": request.name,
                "price": request.price,
                "is_active": request.is_active,
                "updated_at": datetime.now(tz=timezone.utc),
            }
        )
    ).returning(products_table)
    return await database.fetch_one(query)
