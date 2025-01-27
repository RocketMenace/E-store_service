from typing import Any

from app.database.settings import database
from app.shopping_cart.models import carts_table, product_shopping_carts_table


async def get_user_cart(user_id: int) -> int:
    query = carts_table.select().where(carts_table.c.owner == user_id)
    cart = await database.execute(query)
    return cart


async def cart_add_product(
    product_id: int, quantity: int, cart_id: int
) -> dict[str, Any]:
    product_price = await database.execute(
        f"SELECT price FROM products WHERE id = {product_id}"
    )
    query = (
        product_shopping_carts_table.insert().values(
            {
                "cart_id": cart_id,
                "product_id": product_id,
                "quantity": quantity,
                "total_price": product_price * quantity,
            }
        )
        # .returning(product_shopping_carts_table)
    )
    await database.execute(query)
    return await database.fetch_one(query)


async def cart_get_total_price(cart_id: int):
    query = await database.execute(
        f"SELECT SUM(total_price) FROM product_shopping_carts WHERE cart_id = {cart_id}"
    )
    return query


async def cart_delete_product(cart_id: int, product_id: int):
    query = product_shopping_carts_table.delete().where(
        product_shopping_carts_table.c.cart_id == cart_id,
        product_shopping_carts_table.c.product_id == product_id,
    )
    await database.execute(query)


async def cart_clear(cart_id: int):
    query = product_shopping_carts_table.delete().where(
        product_shopping_carts_table.c.cart_id == cart_id
    )
    await database.execute(query)


async def create_shopping_cart(user_id: int) -> None:
    query = carts_table.insert()
    values = {"owner": user_id}
    await database.execute(query, values)
