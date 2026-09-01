from fastapi import FastAPI, Request
import time

app = FastAPI()

# @app.middleware("http") tells FastAPI that the function below should run for every incoming HTTP request.
# Middleware runs BEFORE the request reaches the endpoint and can also run AFTER the endpoint returns a response.
 
@app.middleware('http')
async def log_middleware(request:Request,call_next):
    start_time = time.time()

    response = await call_next(request) # Send the request to the endpoint and wait for its response

    process_time = time.time()-start_time

    print(f"Path:{request.url.path} | Time:{process_time}") # Print the URL path and processing time

    return response   # Send the response back to the client



