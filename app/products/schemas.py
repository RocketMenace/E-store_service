from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    # created_at: datetime
    # updated_at: datetime
    pass


class ProductIn(ProductBase):
    name: str
    price: int
    is_active: bool


class Product(ProductIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
