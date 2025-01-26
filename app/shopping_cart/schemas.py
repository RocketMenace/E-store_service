from pydantic import BaseModel, ConfigDict

from app.products.schemas import Product




class Cart(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    products: list[Product]
    total_price: float
