from databases import Database
from sqlalchemy import MetaData, create_engine

from app.database.config import config

config.DATABASE_URL = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_SERVER}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

metadata = MetaData()
engine = create_engine(config.DATABASE_URL, echo=True)
database = Database(config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK)
