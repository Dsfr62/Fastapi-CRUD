from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from models import User
from users.schemas import CreateUser

class UsersService:
    
    def get_one(id:int, db:Session):
        user:User = db.query(User).filter(User.id == id).first()
        response = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        return response

    def create_one(user:CreateUser, db:Session):
        check_email = db.query(User).filter(User.email == user.email).first()
        if check_email is None:
            new_user: User = User (
                name = user.name,
                email = user.email,
                password = generate_password_hash(user.password)
            )
            db.add(new_user)
            db.commit()
            return new_user
        raise Exception("User email already exists")

    def delete_one(id:int, db:Session):
        to_delete = db.query(User).filter(User.id == id).first()
        db.delete(to_delete)
        db.commit()
        return to_delete