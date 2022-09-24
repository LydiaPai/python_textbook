try:
    f=open("sample.txt", "r", encoding="utf-8") # 當發生無法開啟檔案的例外時…

except FileNotFoundError:
    print("無法開啟檔案。") # 執行 except 區塊

else:  # 當沒有發生例外時，執行else區塊
    lines=f.readlines()
    for line in lines:
        print(line, end="")
    f.close()

finally:  # 不論有沒有發生例外，finally 區塊都會被執行
    print("處理結束了。")