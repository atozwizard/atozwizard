import repository
from sqlalchemy.orm import Session

def create_todo(db: Session, content: str):
    todo = repository.create_todo(db, content) # repository에 db 전달
    return {
        "id": todo.id,
        "content": todo.content,
        "created_at": str(todo.created_at)
    }
    # todo_id = repository.create_todo(db, content)
    # row = repository.get_todo_id(todo_id)
    # return {
    #         "id": row[0],
    #         "content": row[1],
    #         "created_at": str(row[2])
    #     }
    
def list_todos(db: Session):
    todos = repository.get_todos(db)
    return [{
        "id": t.id,
        "content": t.content,
        "created_at": str(t.created_at)
    } for t in todos]
    # rows = repository.get_todos()
    # return repository.get_todos()
    
def delete_todo(db: Session, todo_id: int):
    return repository.delete_todo(db, todo_id)