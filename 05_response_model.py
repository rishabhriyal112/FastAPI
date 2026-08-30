from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

#User Model
class User(BaseModel):
    name:str
    age:int
    password:str

#Response Model
class UserResponse(BaseModel):
    name:str
    age:int

# "response_model" : defines, validates, filters, and formats the data that your API sends back to the client.
@app.get('/users', response_model = UserResponse)
def get_users():
    return {
        "name" : "Rishabh",
        "age":21,
        "password":"12345"
    }

# Output Formatting:
    # Response follows UserResponse structure
    # password is removed from output
