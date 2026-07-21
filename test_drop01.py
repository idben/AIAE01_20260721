from db import get_conn

drop_sql = """
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS categories;
"""

with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.execute(drop_sql)
    conn.commit()

print("資料表刪除成功")