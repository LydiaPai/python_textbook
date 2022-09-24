f=open("sample.txt", "w", encoding="utf-8") # w 開啟要寫入的文字檔案
# open 函數可以傳遞「檔案名稱,開啟模式」的引數 
# 檔案開啟後，會返回代表檔案的實體物件
f.write("您好\n") # 寫入到檔案之中
f.write("再見\n")

f.close() # 關閉檔案