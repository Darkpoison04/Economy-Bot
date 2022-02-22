from utils.database import connection as con

async def user_check(uid):
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM CASH WHERE id = "{uid}"')
    result = cursor.fetchall()
    if len(result) == 0:
        cursor.execute(f"INSERT INTO CASH(id) VALUES({uid})")
        db.commit()

async def table_check():
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CASH(id VARCHAR(255) , cash BIGINT DEFAULT 20000)")
    db.commit()
