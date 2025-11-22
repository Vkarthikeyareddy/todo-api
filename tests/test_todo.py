import os
import sys

# Add project root so we can import todo_api
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_api.todo import (
    list_todos,
    add_todo,
    delete_todo,
    mark_todo_done,
    get_pending_todos,
    get_completed_todos,
)


def test_list_todos_starts_empty():
    todos = []
    assert list_todos(todos) == []


def test_add_todo_adds_item_with_id_and_completed_flag():
    todos = []
    todos, todo = add_todo(todos, "Buy milk", next_id=1)

    assert len(todos) == 1
    assert todo["id"] == 1
    assert todo["title"] == "Buy milk"
    assert todo["completed"] is False


def test_delete_todo_removes_existing_item():
    todos = [
        {"id": 1, "title": "Buy milk", "completed": False},
        {"id": 2, "title": "Read book", "completed": False},
    ]

    todos = delete_todo(todos, todo_id=1)

    assert len(todos) == 1
    assert todos[0]["id"] == 2
    assert todos[0]["title"] == "Read book"


def test_mark_todo_done_sets_completed_flag():
    todos = [
        {"id": 1, "title": "Buy milk", "completed": False},
        {"id": 2, "title": "Read book", "completed": False},
    ]

    todos = mark_todo_done(todos, todo_id=1)

    completed_ids = [t["id"] for t in todos if t["completed"]]
    assert 1 in completed_ids
    assert 2 not in completed_ids


def test_pending_and_completed_split_correctly():
    todos = [
        {"id": 1, "title": "Buy milk", "completed": True},
        {"id": 2, "title": "Read book", "completed": False},
    ]

    pending = get_pending_todos(todos)
    completed = get_completed_todos(todos)

    assert len(pending) == 1
    assert pending[0]["id"] == 2

    assert len(completed) == 1
    assert completed[0]["id"] == 1