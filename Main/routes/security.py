from fastapi import APIRouter
from Main.database_setup import DbManager, Students

security = APIRouter(
    tags=['security'],
    responses={
        404:{
            "message": "not found"
        }
    }
)

@security.get("/testing")
async def get_student(db: DbManager):
    return db.query(Students).all()