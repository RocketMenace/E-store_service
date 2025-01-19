from sqlalchemy import Column, Boolean, Identity, Integer, String, Table, DateTime, Null
from app.database.settings import metadata
from datetime import timezone, datetime

products_table = Table(
    "products",
    metadata,
    Column("id", Integer, Identity(), primary_key=True, index=True),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("created_at", DateTime, default=datetime.now(tz=timezone.utc)),
    Column("updated_at", DateTime, default=Null, onupdate=datetime.now(tz=timezone.utc)),
    Column("is_active", Boolean, default=True, nullable=False)
)