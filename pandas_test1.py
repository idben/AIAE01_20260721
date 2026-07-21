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