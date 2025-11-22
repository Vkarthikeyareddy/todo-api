def list_todos():
    return []

def add_todo(todos, item):
    todos.append(item)
    return todos

def delete_todo(todos, item):
    if item in todos:
        todos.remove(item)
    return todos

def mark_todo_done(todos, item, completed):
    """
    Mark a todo as done by adding it to the completed list if it's in todos.
    We keep todos as a simple list of strings; completed is a separate list.
    """
    if item in todos and item not in completed:
        completed.append(item)
    return completed

def get_pending_todos(todos, completed):
    """
    Return a list of todos that are not in the completed list.
    """
    return [item for item in todos if item not in completed]

