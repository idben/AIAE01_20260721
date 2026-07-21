from db import get_conn

# 新增資料
str_sql = """
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS categories;
"""

with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO categories (name) VALUES (%s) RETURNING id",
            ("3C 電子",),
        )
        categor_id = cursor.fetchone()[0]
    conn.commit()

print(f"新增分類成功: {categor_id}")