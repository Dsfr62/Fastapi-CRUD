from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

dbEngine=create_engine(os.environ.get("DATABASE_URL"),
    echo=True
)

Session=sessionmaker(bind=dbEngine, autocommit=False, autoflush=False)

Base=declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()