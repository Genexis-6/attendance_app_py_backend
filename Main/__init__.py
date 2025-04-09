from fastapi import FastAPI
from .routes import reg_routes


app = FastAPI()
reg_routes(app)
