from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#NORMAL PYDANTIC SCHEMA 
# class User(BaseModel):
#     name : str
#     age : int
#     email : str

# @app.post('/create-user')
# def create_user(user:User):
#     # print(user)
#     return {
#         "message" : "User Created",
#         "data" : user
#     }


#NESTED PYDANTIC SCHEMA
class Address(BaseModel):
    city : str
    pincode : int

class User(BaseModel):
    name : str
    age : int
    address : Address

@app.get('/create-user')
def create_user(user:User):
    return {
        "message" : "User Created",
        "date" : user
    }
