from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    pass


class ProductIn(ProductBase):
    name: str
    price: float
    is_active: bool


class Product(ProductIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
