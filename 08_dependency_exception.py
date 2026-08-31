from fastapi import FastAPI, Depends, Header,HTTPException 

app = FastAPI()

# Dependency function: validates the token from the request header
def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code = 401,
            detail = "Unauthorized"
        )
    return {
        "user" : "Authorized User"
    }

# Dependency Injection: FastAPI executes verify_token() before this function
@app.get("/secure-data")
def secure_data(user= Depends(verify_token)):
    return { 
        "message" : "Secure data accessed",
        "user" : user
    }



# Reusable logic to get the current user
# def get_current_user():
#     return {
#         "user" : "mohit"
#     }

# # FastAPI injects the user using get_current_user
# @app.get('/profile')
# def profile(user= Depends(get_current_user)):
#     return user

# # Reuse the same dependency and inject the user
# @app.get('/dashboard')
# def dashboard(user= Depends(get_current_user)):
#     return user

