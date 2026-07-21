import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)


# series 的基本使用
# 有標籤的一欄資料
scores = pd.Series([80, 90, 75, 60, 95])
print(scores)
print(f"索引值 1 對應的分數是 {scores[1]}")
print("-"*30, "\n")

# series 自定索引
scores = pd.Series(
    [80, 90, 75, 60, 95],
    index=["小安", "小美", "小華", "小杰", "小芳"]
)
print(scores)
print(f"小美的分數是 {scores["小美"]}")
# 昨天才學的 NumPy 中的 mean/max/min/sum 都一樣還在
print(f"平均分數是 {scores.mean()}")
print(f"最高分數是 {scores.max()}")
print(f"最低分數是 {scores.min()}")

# 布林 mask
mask = scores >= 80
print(mask)
print(scores[mask])
print("-"*30, "\n")

# DataFrame 的基本使用
students_df = pd.DataFrame({
    "姓名": ["小安", "小美", "小華", "小杰"],
    "國文": [80, 88, 60, 95],
    "英文": [90, 76, 85, 91],
    "數學": [75, 92, 70, 89],
})
print(students_df, "\n")

# 取用資料
# 取用單一欄位
print(students_df["數學"], "\n")
# 取用複數欄位
print(students_df[["數學", "英文", "國文"]], "\n")
# 英文+人名在左
print(students_df[["姓名", "英文"]], "\n")

# 寫入資料
# axis=1(列)/0(欄)
students_df["平均"] = students_df[["數學", "英文", "國文"]].mean(axis=1).round(1)
print(students_df, "\n")

# 練習 1: students_df 加上總分
students_df["總分"] = students_df[["數學", "英文", "國文"]].sum(axis=1)
print(students_df, "\n")

# 用 iloc 查詢資料
# 用數字(索引), 取出一整列的資料
print(students_df.iloc[0], "\n")
# 使用二維串列(陣列)的取值方式, 再搭配 iloc 取用 DataFrame 單一一格的值
print(students_df.iloc[0, 2], "\n")

# 用 loc 查詢資料
# loc 是用(欄位的) name 去查詢
students_df = students_df.set_index("姓名")
print(students_df, "\n")
print(students_df.loc["小杰"], "\n")
print(students_df.loc["小杰", "數學"], "\n")


# head()/tail()
orders_df = pd.DataFrame({
    "訂單編號": [101, 102, 103, 104, 105, 106, 107, 108],
    "飲料": ["紅茶", "奶茶", "綠茶", "奶茶", "紅茶", "可可", "綠茶", "奶茶"],
    "數量": [2, 1, 3, 2, 1, 2, 4, 1],
    "單價": [30, 45, 35, 45, 30, 50, 35, 45],
})
print(orders_df, "\n")
# .head() 前 5 筆資料，5 可以用參數帶入更換
print(orders_df.head(3), "\n")
# .tail() 後 5 筆資料，5 可以用參數帶入更換
print(orders_df.tail(1), "\n")


# info
# 自帶 print
# 輸出資料表摘要(summary)
orders_df.info()
print("\n")

# describe
# 產生數值摘要
print(orders_df["數量"].describe())
print("\n")
print(orders_df[["數量", "單價"]].describe())
print("\n")


orders_df["小計"] = orders_df["數量"] * orders_df["單價"]
print(orders_df, "\n")


# 練習 3
print(f"訂單小計最高金額是 {orders_df["小計"].max()}")