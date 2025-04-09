from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main.config import settings


engine = create_engine(
    url=settings.DATABASE_URL
)

local_session = sessionmaker(
    bind=engine,
    autoflush=True,
    autocommit=False
)

Base = declarative_base()