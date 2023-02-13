from fastapi import APIRouter, status, Depends

from config import get_db
from users.service import UsersService
from users.schemas import CreateUser

usersRouter = APIRouter(prefix="/users", tags=["Users"])

@usersRouter.get("/{id}", status_code=status.HTTP_200_OK)
async def get_user(id:int, db=Depends(get_db)):
    return UsersService.get_one(id=id, db=db)

@usersRouter.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user:CreateUser, db=Depends(get_db)):
    return UsersService.create_one(user=user, db=db)

@usersRouter.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id:int, db=Depends(get_db)):
    return UsersService.delete_one(id=id, db=db)