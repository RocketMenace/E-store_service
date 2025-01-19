from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductBase(BaseModel):
    created_at: datetime
    updated_at: datetime

class ProductIn(ProductBase):
    name: str
    price: int
    is_active: bool

class Product(ProductIn):
    model_config = ConfigDict(from_attributes=True)
    id: int