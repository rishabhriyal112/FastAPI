from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Home Route
@app.get("/")
def home():
    return {"message" : "Welcome to FastAPI"}

#About Route
@app.get("/about")
def about():
    return {"message" : "This is About Section page"}

#Users Route - Path Parameter
# @app.get("/users/{user_id}")
# def users(user_id : int): #the int means that only the integer no. like 1,2,3 can be used in url for showing specific data not other like string abc , hello etc. Also for string we can "str" instead of "int"
#     return {"user_id":user_id}

#Query Parameter
@app.get("/users")
def get_users(name : str = None):
    return {"Name":name} 

#Default value 
@app.get("/products")
def get_products(limit : int = 10):
    return {"Limit" : limit}

#Multiple params
@app.get("/items")
def get_items(name : str = None, price : int = 0):
    return {"Name" : name, "Price" : price}

#GET Request - To create a user
@app.post('/create-user')
def create_user(name : str, age : int):
    return {
        "Name" : name,
        "Age" : age
    }

#Second GET Request - To create a user : Basically in this case whatever you wanna send like name age location etc things you can send
# @app.post('/create-client')
# def create_client(user:dict):
#     # print(user)
#     return {
#         "message" : "User created",
#         "data" : user
#     }
    
class User(BaseModel):
    name : str
    age : int

@app.get('/create-client')
def create_client(user : User):
    return {
        "message" : "User Created",
        "data" : user
    }
