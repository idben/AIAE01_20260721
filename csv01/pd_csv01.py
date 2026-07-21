import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# 讀取外部 .csv 檔做為資料來源
order_df = pd.read_csv("orders.csv")

print(order_df)