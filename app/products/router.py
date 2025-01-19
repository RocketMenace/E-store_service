from fastapi import APIRouter, status
from app.products.schemas import Product

products_router = APIRouter()


@products_router.post(path="/create", status_code=status.HTTP_201_CREATED, response_model=Product)
async def add_product():
    pass

@products_router.put(path="/{product_id}/update", status_code=status.HTTP_200_OK, response_model=Product)
async def update_product():
    pass

@products_router.delete(path="/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product():
    pass