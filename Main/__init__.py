from fastapi import FastAPI
from .routes import reg_routes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
reg_routes(app)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']
)