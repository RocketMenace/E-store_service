from sqlalchemy import Table, Column, Integer, Identity, String, Boolean
from app.database.settings import metadata

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, Identity(), primary_key=True, index=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("middle_name", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("phone", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column("is_admin", Boolean, default=False, nullable=False)
)
