import repository

def create_todo(content):
    todo_id = repository.create_todo(content)
    row = repository.get_todo_id(todo_id)
    return {
            "id": row[0],
            "content": row[1],
            "created_at": str(row[2])
        }
    
def list_todos():
    rows = repository.get_todos()
    return repository.get_todos()
    
def delete_todo(todo_id):
    return repository.delete_todo(todo_id)