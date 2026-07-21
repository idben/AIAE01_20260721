from db import get_conn

str_sql = """
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS categories;
"""

with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.execute(str_sql)
    conn.commit()

print("資料表刪除成功")