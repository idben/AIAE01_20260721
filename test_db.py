from db import get_conn

with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT version()")
        row = cursor.fetchone()
        print(row[0])