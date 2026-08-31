from fastapi import FastAPI, status, HTTPException

app = FastAPI()

#HTTP Status Code and Custom Status Code
@app.post("/create-user",status_code= status.HTTP_201_CREATED)
def create_user():
    return {"message" : "User Created"}

@app.get("/user")
def get_users():
    return {
        "status" : "Success",
        "message" : "User Fetched",
        "data" : {
            "name" : "Mohit",
            "age" : 21
        }
    }

#Error Handling using HTTPException
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return{
        "id" : 1,
        "name" : "Mohit"
    }
