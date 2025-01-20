from app.database.settings import database
from app.users.models import users_roles


async def fill_roles_table():
    query = users_roles.select()
    if not await database.fetch_one(query):
        values = [{"role_name": "admin"}, {"role_name": "user"}]
        query = users_roles.insert()
        await database.execute_many(query=query, values=values)
