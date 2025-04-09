from fastapi import APIRouter, Form, File, UploadFile
from starlette.responses import JSONResponse

from Main.utils import get_unique_file_name, save_profile, generate_hash_password
from pathlib import Path
from starlette.exceptions import HTTPException
from Main.database_setup import DbManager, Students, RegisterStudent
import json


security = APIRouter(
    tags=['security'],
    responses={
        404:{
            "message": "not found"
        }
    },
    prefix="/security"
)

@security.get("/testing")
async def get_student(db: DbManager):
    return db.query(Students).all()



@security.post("/registration")
async def register_students(
        db: DbManager,
        student_details: str = Form(...),
        file: UploadFile = File(...)
    ):
    try:
        student = RegisterStudent(**json.loads(student_details))
        check_user_exist = db.query(Students).filter(Students.email== student.email).first()
        if check_user_exist:
            raise HTTPException(
                detail="this user already exist",
                status_code=403
            )

        unique_filename = get_unique_file_name(file.filename)
        file_location = save_profile(unique_filename)
        db.add(
            Students(
                firstname = student.firstname,
                lastname = student.lastname,
                email = student.email,
                department = student.department,
                matric = student.matric,
                level = student.level,
                profile_pic= file_location,
                password = generate_hash_password(student.password)
            )
        )
        db.commit()
        db.flush()

        with open(file_location, "wb") as f:
            f.write(await file.read())

        return JSONResponse(
            content="user registered successfully",
            status_code=200
        )

    except json.JSONDecodeError as e:
        raise HTTPException(
            detail=f"invalid json data due to {e}",
            status_code=400
        )


