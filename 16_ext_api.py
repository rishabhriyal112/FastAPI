#Normal Python code using requests from ext api to take data
# import requests 
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()
# print(data[:2])

from fastapi import FastAPI, HTTPException
import requests 
app=FastAPI()

#GET all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

#Get Single Post
@app.get("/posts/{id}")
def get_post(id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=400,detail="Page Not Found")
    return response.json()
    
