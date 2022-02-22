from utils.database import connection as con


async def check_balance(uid):
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute(f'SELECT CASH FROM CASH WHERE id = "{uid}"')
    result = cursor.fetchall()
    for i in result:
        cash = i[0]
    return cash


async def add_balance(uid, amount):
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute(f'UPDATE CASH SET CASH = CASH + {amount} WHERE id = "{uid}"')
    db.commit()


async def remove_balance(uid, amount):
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute(f'UPDATE CASH SET CASH = CASH - {amount} WHERE id = "{uid}"')
    db.commit()
