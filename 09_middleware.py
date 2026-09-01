from fastapi import FastAPI, Request

app = FastAPI()

# @app.middleware("http") tells FastAPI that this function should be used as HTTP middleware.
# Middleware runs for every HTTP request that comes to the application.

@app.middleware('http')
async def my_middleware(
    request : Request, # Incoming request from the client
    call_next          # Function that passes the request to the next handler/endpoint
    ):
    
    print("Request Recieved") # Runs before the request reaches the endpoint

    # call_next() passes the request to the next part of the application.
    # Usually, this means the request goes to the appropriate FastAPI endpoint.
    #'await' is used because call_next() is asynchronous.
    # Pass request to endpoint
    response = await call_next(request)

  
    print("Response Sent")  # Runs after the endpoint sends a response

    
    return response         # Return response to client

