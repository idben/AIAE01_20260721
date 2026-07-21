from db import get_conn
from pathlib import Path

# 新增多筆資料 BY seed.sql
str_sql = Path("seed.sql").read_text(encoding="utf-8")

with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.execute(str_sql)
    conn.commit()

print(f"資料匯入成功")