from db import get_conn

# 新增多筆資料
category_id = 1

products = [
    ("USB-C 傳輸線", 190, 200, category_id),
    ("行動電源", 690, 80, category_id),
    ("手機保護殼", 250, 300, category_id),
]

str_sql = """
INSERT INTO products (name, price, stock, category_id) VALUES (%s, %s, %s, %s) RETURNING id
"""



with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.executemany(
            str_sql,
            products,
        )
        # product_id = cursor.fetchone()[0]
    conn.commit()

print(f"產品新增多個成功")