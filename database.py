from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


# DB 접속 정보 (기존 정보 활용)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://tester:tester@localhost:3306/llmagent"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# ... engine 설정 코드 ...

# 이 코드가 실행되는 순간, Base를 상속받은 모든 모델이 DB 테이블로 생성됨




# DB 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()