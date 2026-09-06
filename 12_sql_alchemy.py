from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app=FastAPI()

#DB URL
DATABASE_URL = "sqlite:///./test.db"

#Engine Create (DB Connection)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

#Session (DB Operation ke liye)
sessionLocal = sessionmaker(bind=engine)

#Base (model ke liye)
Base = declarative_base()

# Table (Model)
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

# Table create
Base.metadata.create_all(bind=engine)

# Dependency (DB session provide karega)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()


#Create API
@app.post("/todos")
def create_todo(title : str, db:Session = Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message" : "Todo Created",
        "data": todo
    }

#Read All Data
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "Total" : len(todos),
        "data" : todos
    }

#Read Particular Data based on id
@app.get("/todos/{todo_id}")
def get_todo(todo_id=int, db:Session= Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="Todo not FOund")
    return todo

#Update Data
@app.put('/todos/{todo_id}')
def update_todo(todo_id:int, title:str, db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not Found")
    
    todo.title = title
    db.commit()
    db.refresh(todo)
    return{
        "message": "Todo Updated",
        "data" : todo
    }

#Delete Data
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not Found")

    db.delete(todo)
    db.commit()
    return{
        "message":"Todo Deleted"
    }

