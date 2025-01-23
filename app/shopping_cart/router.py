from fastapi import APIRouter, status, Depends, Response
from app.shopping_cart.services import cart_add_product, get_user_cart, cart_get_total_price
from app.auth.jwt import check_user_jwt
from app.auth.schemas import TokenData
from app.auth.services import get_user_by_email
from typing import Annotated
from app.shopping_cart.schemas import Cart
from app.products.services import get_product
from app.products.schemas import Product

shopping_cart_router = APIRouter()


@shopping_cart_router.post(path="/add_product", status_code=status.HTTP_200_OK)
async def add_product_in_cart(product_id: int, quantity: int, token: Annotated[TokenData, Depends(check_user_jwt)]):
    current_user = await get_user_by_email(token.email)
    product = await get_product(product_id)
    user_cart = await get_user_cart(current_user.id)
    print(user_cart, "***************")
    result = await cart_add_product(product_id, quantity, user_cart)
    print(result, "^^^^^^^^^^^^^^")
    return Cart(products=list[Product], total_price=cart_get_total_price(quantity, product.price))



@shopping_cart_router.put(path="/remove_product/{product_id}")
async def cart_remove_product():
    pass

@shopping_cart_router.put(path="/clear_cart")
async def cart_clear_products():
    pass

