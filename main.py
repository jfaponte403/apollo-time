from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routes.login_route import login

app = FastAPI()  # Change this line

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login, prefix="/login")
