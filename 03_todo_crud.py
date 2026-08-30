from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    completed : bool

#CRUD OPERATIONS

#CREATE - Using POST Request
@app.post('/todos')
def create_todos(todo:Todo):
    todos.append(todo)
    return {"message" : "TODO added", "data" : todo}
 
# READ ALL - Using GET Request
@app.get("/todos") 
def get_todos():    
    return todos

#READ ONE - Using GET Request
@app.get('/todos/{todo_id}')
def get_todo(todo_id : int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error" : "Todo not found"}

#MODIFY - Using PUT Request
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updatedTodo : Todo):
    # enumerate(todos) gives us both:  index -> position of the todo in the list. todo -> actual Todo object
    # Example:  index = 0 todo = Todo(id=1, ...) and  index = 1 todo = Todo(id=2, ...)
    for index , todo in enumerate (todos):
        # If current todo has id = 2, # we found the todo we want to update.
        # if todo.id == todo_id: # Replace the old todo with the new todo # todos[index] -> old todo 
        # updatedTodo -> new todo 
        # Example: # Before: # todos[1] = Todo(id=2, title="Learn Python", completed=False) 
        # After: # todos[1] = Todo(id=2, title="Learn FastAPI", completed=True) todos[index] = updatedTodo
        if todo.id == todo_id:
            todos[index] = updatedTodo
            return{
                "message" : "Data Updated",
                "data" : updatedTodo
            }
    return {"error" : "Todo not found"}

#DELETE : Using DELETE Request
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id : int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message" : "Data Deleted"}
    return {"error" : "Todo not found"}
