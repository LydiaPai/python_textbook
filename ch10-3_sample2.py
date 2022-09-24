import json
f=open("sample.json", "r", encoding="utf-8")
data=json.load(f) # 讀取 json 檔案
print(data) 
f.close()
