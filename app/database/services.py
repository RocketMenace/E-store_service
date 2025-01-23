from app.auth.security import hash_password
from app.database.config import config
from app.database.settings import database
from app.users.models import users_roles, users_table


async def fill_roles_table():
    query = users_roles.select()
    if not await database.fetch_one(query):
        values = [{"role_name": "admin"}, {"role_name": "user"}]
        query = users_roles.insert()
        await database.execute_many(query=query, values=values)


async def create_admin():
    query = users_table.select().where(users_table.c.role == 1)
    if not await database.fetch_one(query):
        query = users_table.insert()
        values = {
            "first_name": "Admin",
            "last_name": "FastAPI",
            "middle_name": "superuser",
            "email": "admin@gmail.com",
            "phone": "+74568529632",
            "role": 1,
            "password": hash_password(config.ADMIN_PASSWORD),
        }
        await database.execute(query, values)
