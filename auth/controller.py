from fastapi import APIRouter, status, Depends, exceptions
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash

from config import get_db
from auth.schemas import LoginSchema
from models import User

authRouter = APIRouter(prefix="/auth", tags=["Authentication"])

@authRouter.post("/login", status_code=status.HTTP_200_OK)
async def login(user:LoginSchema, Authorize:AuthJWT=Depends(), db:Session=Depends(get_db)):
    dbUser:User = db.query(User).filter(User.email == user.email).first()
    if dbUser is not None:
        password_check = check_password_hash(dbUser.password, user.password)
        if password_check:
            access_token = Authorize.create_access_token(subject=dbUser.id)
            response = {
                "access": access_token
            }
            return response
        else:
            raise exceptions.HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
    else:
        raise exceptions.HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is not registered to any user")

@authRouter.get("/", status_code=status.HTTP_200_OK)
async def auth_user(Authorize:AuthJWT=Depends(), db:Session=Depends(get_db)):
    try:
        Authorize.get_jwt_subject()
    except:
        raise exceptions.HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user: User = db.query(User).filter(User.id == Authorize.get_jwt_subject()).first()
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }