import csv # 匯入 csv(Comma Seperated Value) 模組
f=open("sample.csv", "r", encoding="utf-8") # 讀取 csv 檔案
# 讀取 csv 檔案是由「reader」這個實體物件來處理， reader 會成為返回 csv 檔案各列資料的迭代器
rd=csv.reader(f) # 取得reader
for row in rd: # 取出1列的資料
     for col in row: # 取出該列的1個項目
        print(col, end="")
    print()
f.close()