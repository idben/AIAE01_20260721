import psycopg

# 最基本的連線

conn_params = {
    "host": "localhost",
    "port": 5432,
    "dbname": "shop",
    "user": "postgres",
    "password": "a123456",
}

# conn = psycopg.connect(**conn_params)
# cursor = conn.cursor()
# cursor.execute("SELECT version()")
# row = cursor.fetchone()
# print(row[0])
# cursor.close()
# conn.close()
with psycopg.connect(**conn_params) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT version()")
        row = cursor.fetchone()
        print(row[0])