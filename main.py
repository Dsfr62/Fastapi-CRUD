from fastapi import FastAPI, status

from config import Base, dbEngine
from models import *
from books.controller import booksRouter

app = FastAPI()

Base.metadata.create_all(bind=dbEngine)

@app.get("/", status_code=status.HTTP_200_OK)
async def main():
    return {"message": "Export db with sqlalchemy"}

app.include_router(booksRouter)