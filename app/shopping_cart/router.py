from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.auth.jwt import check_user_jwt
from app.auth.schemas import TokenData
from app.auth.services import get_user_by_email
from app.products.services import get_product
from app.shopping_cart.schemas import Cart
from app.shopping_cart.services import (
    cart_add_product,
    cart_clear,
    cart_delete_product,
    cart_get_total_price,
    get_user_cart,
)

shopping_cart_router = APIRouter()


@shopping_cart_router.post(
    path="/add_product",
    status_code=status.HTTP_200_OK,
    response_model=Cart,
    summary="Add product in shopping cart.",
    response_description="On successful adding product, the API will respond with a 200 status code and the details of the added product in JSON format.",
)
async def add_product_in_cart(
    product_id: int, quantity: int, token: Annotated[TokenData, Depends(check_user_jwt)]
):
    """
    This endpoint allows authorized users to add a new product in their cart.
    The product details must be provided in the request body.
    Upon successful adding, the endpoint returns the details of the newly added product and cart total cost.
    - **product_id**
    - **quantity**
    """
    current_user = await get_user_by_email(token.email)
    product = await get_product(product_id)
    user_cart = await get_user_cart(current_user.id)
    result = await cart_add_product(product_id, quantity, user_cart)
    return Cart(products=[product], total_price=await cart_get_total_price(user_cart))


@shopping_cart_router.delete(path="/remove_product", summary="Delete product from cart")
async def cart_remove_product(
    product_id: int, token: Annotated[TokenData, Depends(check_user_jwt)]
):
    """
    This endpoint allows authorized users to delete a product from their cart.
    The product details must be provided in the request body.
    - **product_id** product_id
    """
    current_user = await get_user_by_email(token.email)
    user_cart = await get_user_cart(current_user.id)
    return await cart_delete_product(user_cart, product_id)


@shopping_cart_router.delete(
    path="/clear_cart",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete all product from cart.",
)
async def cart_clear_products(token: Annotated[TokenData, Depends(check_user_jwt)]):
    """
    This endpoint allows authorized users to delete all products from their cart.
    """
    current_user = await get_user_by_email(token.email)
    user_cart = await get_user_cart(current_user.id)
    return await cart_clear(user_cart)
