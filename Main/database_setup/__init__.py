from .database import engine, Base, local_session
from .model import Students
from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()



DbManager = Annotated[Session, Depends(get_db)]