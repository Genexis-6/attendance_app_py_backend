import uuid
import os
from passlib.context import CryptContext



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