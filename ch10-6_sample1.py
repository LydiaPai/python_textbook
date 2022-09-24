import datetime
dt=datetime.datetime.now()
print("現在是", dt, "。")
# 取得代表日期時間的資料屬性
print("年：", dt.year)
print("月：", dt.month)
print("日：", dt.day)
dt=dt+datetime.timedelta(days=1)
print("1天後為", dt, "。")