import os
import sys

# Add project root (folder that contains `todo_api/`) to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_api.todo import list_todos, add_todo, delete_todo, mark_todo_done

def test_list_todos_starts_empty():
    assert list_todos() == []

def test_add_todo_adds_item():
    todos = []
    updated = add_todo(todos, "Buy milk")
    assert "Buy milk" in updated

def test_delete_todo_removes_existing_item():
    todos = ["Buy milk", "Read book"]
    updated = delete_todo(todos, "Buy milk")
    assert "Buy milk" not in updated

def test_delete_todo_does_nothing_if_not_present():
    todos = ["Buy milk"]
    updated = delete_todo(todos, "Go gym")
    assert updated == ["Buy milk"]

def test_mark_todo_done_adds_item_to_completed():
    todos = ["Buy milk", "Read book"]
    completed = []
    updated_completed = mark_todo_done(todos, "Buy milk", completed)
    assert "Buy milk" in updated_completed

def test_mark_todo_done_ignores_missing_item():
    todos = ["Buy milk"]
    completed = []
    updated_completed = mark_todo_done(todos, "Go gym", completed)
    assert updated_completed == []
