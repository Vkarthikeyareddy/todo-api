# todo_api/todo.py

from typing import List, Dict, Tuple


Todo = Dict[str, object]  # {"id": int, "title": str, "completed": bool}


def list_todos(todos: List[Todo]) -> List[Todo]:
    return todos


def add_todo(todos: List[Todo], title: str, next_id: int) -> Tuple[List[Todo], Todo]:
    todo = {"id": next_id, "title": title, "completed": False}
    todos.append(todo)
    return todos, todo


def delete_todo(todos: List[Todo], todo_id: int) -> List[Todo]:
    return [t for t in todos if t["id"] != todo_id]


def mark_todo_done(todos: List[Todo], todo_id: int) -> List[Todo]:
    for t in todos:
        if t["id"] == todo_id:
            t["completed"] = True
            break
    return todos


def get_pending_todos(todos: List[Todo]) -> List[Todo]:
    return [t for t in todos if not t["completed"]]


def get_completed_todos(todos: List[Todo]) -> List[Todo]:
    return [t for t in todos if t["completed"]]
