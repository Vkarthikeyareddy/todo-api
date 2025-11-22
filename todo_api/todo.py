def list_todos():
    return []

def add_todo(todos, item):
    todos.append(item)
    return todos

def delete_todo(todos, item):
    if item in todos:
        todos.remove(item)
    return todos

#adding comment line
