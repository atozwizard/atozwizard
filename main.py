from fastapi import FastAPI, Request, HTTPException, Depends
import service

# main.py
import models
from database import engine, get_db, Base
from sqlalchemy.orm import Session

# 서버가 뜰 때 테이블이 없으면 자동으로 생성해줌
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ---------------------------
# CREATE
# ---------------------------
@app.post("/todos")
async def create_todo(request: Request, db: Session = Depends(get_db)):
    body = await request.json()
    content = body.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="content is required")
    return service.create_todo(db, content)

    
# ---------------------------
# READ
# ---------------------------
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    return service.list_todos(db)


# ---------------------------
# DELETE
# ---------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    affected = service.delete_todo(db, todo_id)
    if affected == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}