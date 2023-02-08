from pydantic import BaseModel
from typing import Optional

class CreateBookSchema(BaseModel):
    name:str
    stars:Optional[int]=0
    my_opinion:Optional[str]
    is_read:Optional[bool]=False

class UpdateBookSchema(BaseModel):
    name:Optional[str]
    stars:Optional[int]
    my_opinion:Optional[str]
    is_read:Optional[bool]