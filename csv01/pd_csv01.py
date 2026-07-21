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
print("-"*40, "\n")


# 欄位的運算
order_df["小計"] = order_df["數量"] * order_df["單價"]
print(order_df, "\n")


# 篩選: 下條件
# 布林 mask

condition = order_df["數量"] >= 2
result_df = order_df[condition]
print("數量大於兩杯的有: ")
print(result_df)

# 練習 1: \
# condition1 取出單價大於等於 40 元的資料
# condition2 取出小計大於等於 100 元的資料
print("-"*40, "\n")


# 複數條件
# 而且 &
is_milk_tea = order_df["品名"] == "奶茶"
is_qty_enough = order_df["數量"] >= 2
filtered_df = order_df[is_milk_tea & is_qty_enough]
print("是奶茶而且兩杯(含)以上的訂單有: ")
print(filtered_df)
print("-"*40, "\n")

# 或者 |
is_black_tea = order_df["品名"] == "紅茶"
is_price_45 = order_df["單價"] >= 45
filtered2_df = order_df[is_black_tea | is_price_45]
print("是紅茶, 或是單價大於等於 45 元的訂單有")
print(filtered2_df)
print("-"*40, "\n")

# 預設由小到大 ascending=True
print(order_df.sort_values("數量", ascending=True), "\n")

# 練習 2
print(order_df[order_df["小計"] >= 80])