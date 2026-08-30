from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

#Path + Query + Body Combo

# REQUEST BODY MODEL - This class defines the data that we expect inside the REQUEST BODY.
class User(BaseModel):
    name : str
    age : int

@app.post('/users')
def create_user(user:User):
    users.append(user)
    return {"message":"User Created","data":user}

@app.get('/users')
def get_users():
    return users

# PATH + QUERY + BODY COMBINATION
@app.put("/users/{user_id}")
def updated_user(user_id : int, user:User, notify:bool=False):
    if user_id < len(users):
        users[user_id] = user
        return {"message" : "User Updated", "notify" : notify,"data":user}
    return {"error":"User not found"}
