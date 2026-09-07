from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config15 import settings
# import os
# from dotenv import load_dotenv

app = FastAPI()

# load_dotenv()

#Allowed Origin (Frontend URL)
origins = settings.origins

# SECRET_KEY = os.getenv("SECRET_KEY")
# DB_URL = os.getenv("DB_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, #Allowed Frontend
    allow_credentials = True,
    allow_methods = ["*"], #GET, POST, PUT, DELETE
    allow_headers = ["*"]
)

@app.get("/")
def home():
    return { 
        "message" : "CORS Enable API"
    }

#Now connect the Backend localhost URL with a frontend like Reactjs and it will give you a message that are provided in the code.
