# todo_api/api.py

from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool


app = FastAPI(title="Todo API", version="1.0.0")

# Allow requests from your frontend (http://localhost:5500, file://, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # OK for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store – real apps would use a DB
TODOS: List[dict] = []
NEXT_ID = 1


@app.get("/todos", response_model=List[TodoResponse])
def get_todos():
    return TODOS


@app.post("/todos", response_model=TodoResponse)
def create_todo(payload: TodoCreate):
    global NEXT_ID, TODOS
    todo = {"id": NEXT_ID, "title": payload.title, "completed": False}
    NEXT_ID += 1
    TODOS.append(todo)
    return todo


@app.delete("/todos/{todo_id}", response_model=List[TodoResponse])
def delete_todo(todo_id: int):
    global TODOS
    existing_ids = {t["id"] for t in TODOS}
    if todo_id not in existing_ids:
        raise HTTPException(status_code=404, detail="Todo not found")

    TODOS = [t for t in TODOS if t["id"] != todo_id]
    return TODOS


@app.post("/todos/{todo_id}/complete", response_model=List[TodoResponse])
def complete_todo(todo_id: int):
    global TODOS
    existing_ids = {t["id"] for t in TODOS}
    if todo_id not in existing_ids:
        raise HTTPException(status_code=404, detail="Todo not found")

    for t in TODOS:
        if t["id"] == todo_id:
            t["completed"] = True
            break

    return TODOS


@app.get("/todos/pending", response_model=List[TodoResponse])
def get_pending():
    return [t for t in TODOS if not t["completed"]]


@app.get("/todos/completed", response_model=List[TodoResponse])
def get_completed():
    return [t for t in TODOS if t["completed"]]
