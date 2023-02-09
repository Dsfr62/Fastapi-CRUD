from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from config import get_db
from books.service import BookService
from books.schemas import CreateBookSchema, UpdateBookSchema
from helpers.exportdb import export_table

booksRouter = APIRouter(prefix="/books", tags=["Books"])

@booksRouter.get("/", status_code=status.HTTP_200_OK)
async def get_all(db:Session=Depends(get_db)):
    return BookService.get_all(db=db)

@booksRouter.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one(id:int, db:Session=Depends(get_db)):
    return BookService.get_one(id=id, db=db)

@booksRouter.get("/filter/{stars}", status_code=status.HTTP_200_OK)
async def get_by_stars(stars:int, db:Session=Depends(get_db)):
    return BookService.get_by_stars(data=stars, db=db)

@booksRouter.get("/service/export", status_code=status.HTTP_200_OK)
async def export_books():
    return export_table(tablename="books")

@booksRouter.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book:CreateBookSchema, db:Session=Depends(get_db)):
    return BookService.create(data=book, db=db)

@booksRouter.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_book(id:int, bookUpdate:UpdateBookSchema, db:Session=Depends(get_db)):
    return BookService.update_book(id=id, data=bookUpdate, db=db)

@booksRouter.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_book(id:int, db:Session=Depends(get_db)):
    return BookService.delete_book(id=id, db=db)