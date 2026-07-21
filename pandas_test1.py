import pandas as pd

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