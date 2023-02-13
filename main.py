from fastapi import FastAPI, status
from fastapi_jwt_auth import AuthJWT

from auth.config import Settings
from config import Base, dbEngine
from models import *
from books.controller import booksRouter
from users.controller import usersRouter
from auth.controller import authRouter

app = FastAPI()

Base.metadata.create_all(bind=dbEngine)

@AuthJWT.load_config
def get_jwt_config():
    return Settings()

@app.get("/", status_code=status.HTTP_200_OK)
async def main():
    return {"message": "Basic JWT Authentication"}

app.include_router(booksRouter)
app.include_router(usersRouter)
app.include_router(authRouter)