from sqlalchemy import (Column, DateTime, ForeignKey, Identity, Integer,
                        String, Table, func)

from app.database.settings import metadata

tokens = Table(
    "auth_token",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("token_data", String, nullable=False),
    Column("expires_at", DateTime, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)
