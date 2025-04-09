import uuid
import os
from passlib.context import CryptContext
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from Main.database_setup import Students

pwd_context = CryptContext(schemes="bcrypt", deprecated='auto')

def get_unique_file_name(filename: str):
    base_name, ext = os.path.splitext(filename)
    unique_name = f"{uuid.uuid4().hex}{ext}"
    return unique_name


def save_profile(unique_name: str):
    file_location = os.path.join("upload", unique_name)
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    return file_location.replace("\\", "/")


def generate_hash_password(password):
    return pwd_context.hash(password)


def verify_hash_password(hash_pass, password):
    return pwd_context.verify(password, hash=hash_pass)

def authenticate_student(db, matric: str, password: str):
    check_student = db.query(Students).filter(Students.matric == matric).first()
    if check_student:
        if verify_hash_password(hash_pass=check_student.password, password=password):
            return JSONResponse(
                status_code=200,
                content="user authenticated"
            )
        raise HTTPException(
            detail="invalid password",
            status_code=401
        )
    raise HTTPException(
        detail="no user with this detail found",
        status_code=404
    )
