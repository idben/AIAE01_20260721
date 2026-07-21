import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# 讀取外部 .csv 檔做為資料來源
order_df = pd.read_csv("orders.csv")

print(order_df.head(2))
print("-"*40, "\n")
print(order_df.tail(2))
print("-"*40, "\n")
order_df.info()
print("-"*40, "\n")
print(order_df.columns.tolist())
print("-"*40, "\n")

# 更改欄位名稱
order_df = order_df.rename(columns={"飲料": "品名"})

print(order_df["品名"])
print("-"*40, "\n")
print(order_df)
print("-"*40, "\n")

# 更改欄位名稱: 改英文欄位名稱
orders2_df = pd.read_csv("orders_en.csv")

renamed_df = orders2_df.rename(columns={
    "order_id": "訂單編號",
    "item": "品名",
    "qty": "數量",
    "price": "單價"
})

print(renamed_df)