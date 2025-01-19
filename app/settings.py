import os
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Diretório base do app

class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "menuMaster2.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")