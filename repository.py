
import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="tester",
        password="tester",
        database="llmagent"
    )   
    
def create_todo(content):      
    conn = get_db()
    cursor = conn.cursor()
    # 👉 학생이 작성해야 하는 SQL
    # INSERT 문 작성
    # 예: INSERT INTO todo (content) VALUES (%s)
    cursor.execute("INSERT INTO todo (content) VALUES (%s)",
        ### TODO: 여기에 INSERT SQL 작성 ###         
        (content,),
    )
    conn.commit()
    todo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return todo_id

def get_todo_id(todo_id):
    conn = get_db()
    cursor = conn.cursor()
        # 👉 학생이 작성해야 하는 SQL
    # SELECT 문 작성하여 방금 만든 todo 조회
    cursor.execute("SELECT * FROM todo WHERE id = %s",
        ### TODO: 여기에 SELECT SQL 작성 ###        
        (todo_id,),
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

def get_todos():
    conn = get_db()
    cursor = conn.cursor()
    # 👉 학생이 작성해야 하는 SQL
    # 전체 todo 조회 SELECT 문 작성
    cursor.execute(
        ### TODO: 여기에 전체 조회 SELECT SQL 작성 ###
        "SELECT * FROM todo",
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": r[0],
            "content": r[1],
            "created_at": str(r[2])
        }
        for r in rows
    ]


def delete_todo(todo_id: int):
    conn = get_db()
    cursor = conn.cursor()
    # 👉 학생이 작성해야 하는 SQL
    # 삭제 DELETE 문 작성
    cursor.execute("DELETE FROM todo WHERE id = %s"
        ### TODO: 여기에 DELETE SQL 작성 ###
        ,
        (todo_id,),
    )
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected