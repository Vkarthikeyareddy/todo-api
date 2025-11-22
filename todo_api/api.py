# todo_api/api.py

from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from todo_api.todo import (
    list_todos,
    add_todo,
    delete_todo,
    mark_todo_done,
    get_pending_todos,
    get_completed_todos,
)


class TodoCreate(BaseModel):
    title: str


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool


app = FastAPI(title="Todo API", version="1.0.0")

# In-memory store – in real life this would be a DB
TODOS: List[dict] = []
NEXT_ID = 1


@app.get("/todos", response_model=List[TodoResponse])
def get_todos():
    return list_todos(TODOS)


@app.post("/todos", response_model=TodoResponse)
def create_todo(payload: TodoCreate):
    global NEXT_ID, TODOS
    TODOS, todo = add_todo(TODOS, payload.title, NEXT_ID)
    NEXT_ID += 1
    return todo


@app.delete("/todos/{todo_id}", response_model=List[TodoResponse])
def delete_todo_endpoint(todo_id: int):
    global TODOS
    existing_ids = {t["id"] for t in TODOS}
    if todo_id not in existing_ids:
        raise HTTPException(status_code=404, detail="Todo not found")

    TODOS = delete_todo(TODOS, todo_id)
    return TODOS


@app.post("/todos/{todo_id}/complete", response_model=List[TodoResponse])
def complete_todo(todo_id: int):
    global TODOS
    existing_ids = {t["id"] for t in TODOS}
    if todo_id not in existing_ids:
        raise HTTPException(status_code=404, detail="Todo not found")

    TODOS = mark_todo_done(TODOS, todo_id)
    return TODOS


@app.get("/todos/pending", response_model=List[TodoResponse])
def get_pending():
    return get_pending_todos(TODOS)


@app.get("/todos/completed", response_model=List[TodoResponse])
def get_completed():
    return get_completed_todos(TODOS)
