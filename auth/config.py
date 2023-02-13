from pydantic import BaseModel
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Settings(BaseModel):
    authjwt_secret_key = getenv("JWT_SECRET_KEY")