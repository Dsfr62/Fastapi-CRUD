from config import Base
from sqlalchemy import Column, Integer, Text, Boolean, String, DateTime
from datetime import datetime

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(512), nullable=False)
    stars = Column(Integer, default=0)
    my_opinion = Column(Text, nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(256), nullable=True)
    email = Column(String(256), nullable=False)
    password = Column(String(512), nullable=False)
    created_at = Column(DateTime, default=datetime.now())