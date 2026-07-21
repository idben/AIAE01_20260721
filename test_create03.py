from db import get_conn

# 新增資料
str_sql = """
INSERT INTO products (name, price, stock, category_id) VALUES (%s, %s, %s, %s) RETURNING id
"""

category_id = 1

with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            str_sql,
            ("藍牙耳機", 1290, 50, category_id),
        )
        product_id = cursor.fetchone()[0]
    conn.commit()

print(f"產品新增成功: {product_id}")