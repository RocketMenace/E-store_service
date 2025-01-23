from typing import Any

from app.shopping_cart.models import carts_table, product_shopping_carts_table
from app.shopping_cart.schemas import Cart
from app.database.settings import database
from app.products.schemas import Product


async def get_user_cart(user_id: int) -> int:
    query = carts_table.select().where(carts_table.c.owner == user_id)
    cart = await database.execute(query)
    return cart

async def cart_add_product(product_id: int, quantity: int, cart_id: int) -> dict[str, Any]:
    query = product_shopping_carts_table.insert().values(
        {"cart_id": cart_id, "product_id": product_id, "quantity": quantity}
    ).returning(product_shopping_carts_table)
    # values =
    return await database.fetch_one(query)

def cart_get_total_price(quantity: int, price: float) -> float:
    return quantity * price

async def cart_show_products():
    ...

async def cart_delete_product():
    ...

async def cart_clear():
    ...


async def create_shopping_cart(user_id: int) -> None:
    query = carts_table.insert()
    values = {"owner": user_id}
    await database.execute(query, values)

