from sqlalchemy.orm import Session

from models import Book
from books.schemas import CreateBookSchema, UpdateBookSchema

class BookService:
    def get_all(db:Session):
        return db.query(Book).all()
    
    def get_one(id:int, db:Session):
        return db.query(Book).filter(Book.id == id).first()
    
    def get_by_stars(data:int, db:Session):
        return db.query(Book).filter(Book.stars == data).all()
    
    def create(data:CreateBookSchema, db:Session):
        new_book = Book(
            name=data.name,
            stars=data.stars,
            my_opinion=data.my_opinion,
            is_read=data.is_read
        )
        db.add(new_book)
        db.commit()
        return data
    
    def update_book(id:int, data:UpdateBookSchema, db:Session):
        updateData = data.dict(exclude_unset=True)
        db.query(Book).filter(Book.id == id).update(updateData, synchronize_session=False)
        db.commit()
        return data
    
    def delete_book(id:int, db:Session):
        deleteData = db.query(Book).filter(Book.id == id).first()
        db.delete(deleteData)
        db.commit()
        return deleteData
