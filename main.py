from fastapi import FastAPI, Request, HTTPException, Depends
import service

# main.py
import models
from database import engine, get_db, Base
from sqlalchemy.orm import Session

from loguru import logger
import sys

import time
from fastapi import Request

app = FastAPI()

# 로그 설정: 콘솔 출력 및 파일 저장 (log/server.log)
logger.remove() # 기본 핸들러 제거
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:7}</level> | <cyan>{message}</cyan>", colorize=True)
logger.add("logs/server.log", rotation="10 MB", retention="10 days", level="INFO")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    # --- Step 1-B. Request 로깅 ---
    logger.info(f"🚀 Request: {request.method} {request.url.path}")
    logger.info(f"📋 Headers: Host={request.headers.get('host')}, User-Agent={request.headers.get('user-agent')}")
    
    if request.query_params:
        logger.info(f"🔍 Query Params: {dict(request.query_params)}")

# 실행 시간 측정 시작
    start_time = time.time()
    
    # 실제 API 로직 실행
    response = await call_next(request)
    
    # 실행 시간 계산
    process_time = (time.time() - start_time) * 1000

    # --- Step 1-C. Response 로깅 ---
    logger.info(f"✅ Response: Status={response.status_code} | Time={process_time:.2f}ms")
    logger.info(f"📦 Response Headers: Content-Type={response.headers.get('content-type')}")

    return response

# 서버가 뜰 때 테이블이 없으면 자동으로 생성해줌
Base.metadata.create_all(bind=engine)



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