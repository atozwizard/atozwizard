#models.py 신규생성
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base #database.py 에서 정의할 base

class Todo(Base):
    __tablename__ = "todo"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())