import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from todo_api.api import app, TODOS


client = TestClient(app)


def setup_function():
    # Reset in-memory store before each test
    TODOS.clear()
    # We don't reset NEXT_ID here; for a simple demo it's fine if IDs keep increasing


def test_create_and_list_todos():
    # Create a todo
    response = client.post("/todos", json={"title": "Buy milk"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy milk"
    assert data["completed"] is False

    # List todos
    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 1
    assert todos[0]["title"] == "Buy milk"


def test_complete_todo_and_filter_completed():
    # Create two todos
    r1 = client.post("/todos", json={"title": "Buy milk"})
    r2 = client.post("/todos", json={"title": "Read book"})
    todo1 = r1.json()
    todo2 = r2.json()

    # Mark first as completed
    response = client.post(f"/todos/{todo1['id']}/complete")
    assert response.status_code == 200

    # Completed endpoint shows only completed
    response = client.get("/todos/completed")
    completed = response.json()
    assert len(completed) == 1
    assert completed[0]["id"] == todo1["id"]

    # Pending endpoint shows only pending
    response = client.get("/todos/pending")
    pending = response.json()
    assert len(pending) == 1
    assert pending[0]["id"] == todo2["id"]


def test_delete_todo():
    # Create a todo
    r = client.post("/todos", json={"title": "Buy milk"})
    todo = r.json()

    # Delete it
    response = client.delete(f"/todos/{todo['id']}")
    assert response.status_code == 200
    todos = response.json()
    assert todos == []

    # Deleting again should give 404
    response = client.delete(f"/todos/{todo['id']}")
    assert response.status_code == 404
