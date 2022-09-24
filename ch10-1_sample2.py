f=open("sample.txt", "r", encoding="utf-8") # 在讀取模式中開啟檔案
lines=f.readlines() # 讀取所有的列
for line in lines: # 逐列反覆取出
    print(line, end="") # 
f.close()