from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    origins = os.getenv("ORIGINS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DB_URL = os.getenv("DB_URL")

settings = Settings()
