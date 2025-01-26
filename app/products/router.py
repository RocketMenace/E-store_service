from fastapi import APIRouter, Depends, status

from app.auth.jwt import check_admin_access
from app.products.schemas import Product, ProductIn
from app.products.services import create_product, edit_product, remove_product

products_router = APIRouter()


@products_router.post(
    path="/create",
    status_code=status.HTTP_201_CREATED,
    response_model=Product,
    dependencies=[Depends(check_admin_access)],
    summary="Add product to database",
    response_description="On successful creation, the API will respond with a 201 Created status code and the details of the created product in JSON format.",
)
async def add_product(request: ProductIn):
    """
    This endpoint allows admin users to create a new product in the database.
    The product details must be provided in the request body.
    Upon successful creation, the endpoint returns the details of the newly created product.
    - **name** product name
    - **price** product price
    - **is_active** product status
    """
    product = await create_product(request)
    return product


@products_router.put(
    path="/update/{product_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(check_admin_access)],
    summary="Updates product data.",
    response_description="On successful update operation, the API will respond with a 200 status code and the details of the updated product in JSON format."
)
async def update_product(product_id: int, request: ProductIn):
    """
    This endpoint allows admin users to update product data in the database.
    The product details must be provided in the request body.
    Upon successful update operation, the endpoint returns the details of the updated product.
    - **name** product name
    - **price** product price
    - **is_active** product status
    """
    product = await edit_product(product_id, request)
    return product


@products_router.delete(
    path="/delete/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(check_admin_access)],
    summary="Delete product from database.",
    response_description="On successful delete operation, the API will respond with a 204 status code"
)
async def delete_product(product_id: int):
    """
    This endpoint allows admin users to delete product from database.
    The product details must be provided in the request body.
    - **product_id** product id
    """
    await remove_product(product_id)
