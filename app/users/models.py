from sqlalchemy import (Boolean, Column, ForeignKey, Identity, Integer, String,
                        Table)

from app.database.settings import metadata

users_roles = Table(
    "roles",
    metadata,
    Column("id", Integer, Identity(), primary_key=True, index=True),
    Column("role_name", String, nullable=False, unique=True),
)

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
    Column(
        "role",
        Integer,
        ForeignKey("roles.id", ondelete="CASCADE"),
        server_default="2",
        nullable=False,
    ),
)
