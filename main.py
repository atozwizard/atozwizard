from fastapi import FastAPI, Request, HTTPException
import service

app = FastAPI()

# ---------------------------
# CREATE
# ---------------------------
@app.post("/todos")
async def create_todo(request: Request):
    body = await request.json()
    content = body.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="content is required")
    return service.create_todo(content)

    
# ---------------------------
# READ
# ---------------------------
@app.get("/todos")
def get_todos():
    return service.list_todos()


# ---------------------------
# DELETE
# ---------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    affected = service.delete_todo(todo_id)
    if affected == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}