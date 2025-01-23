from app.products.schemas import Product
from pydantic import BaseModel, ConfigDict


# class CartIn(BaseModel):
#     products: list[Product]


class Cart(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    products: list[Product]
    total_price: float

