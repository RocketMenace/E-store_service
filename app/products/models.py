from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Identity,
    Integer,
    String,
    Table,
    func,
)

from app.database.settings import metadata

products_table = Table(
    "products",
    metadata,
    Column("id", Integer, Identity(), primary_key=True, index=True),
    Column("name", String, nullable=False, unique=True),
    Column("price", Float, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime(timezone=True), nullable=True),
    Column("is_active", Boolean, default=True, nullable=False),
)
