import os 
import os.path

curdir=os.listdir(".")

for name in curdir:
    print(os.path.abspath(name), end=",")
    if(os.path.isfile(name)):
        print("是檔案。")
    else:
        print("是目錄。")
print()