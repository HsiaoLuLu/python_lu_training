#讀取全部文字： 檔案物件.read()
#一次讀取一行： for 變數 in 檔案物件： 從檔案依序讀取每行文字到變數中
#讀取json格式： import json 讀取到的資料=json.load(檔案物件)
#寫入json格式： import json json.dump(要寫入的資料,檔案物件)

#with open(檔案路徑, mode=開啟模式) as 檔案物件: 讀取或寫入檔案的程式
#以上區塊會自動,安全的關閉檔案

# #儲存檔案
# #開啟檔案基本語法： 檔案物件=open(檔案路徑,mode=開啟模式)
# 開啟模式： 讀取模式 r,寫入模式 w,讀寫模式 r+
file=open("data.txt",mode="w") #開啟

#寫入文字： 檔案物件.write(字串)
#寫入換行符號： 檔案物件.write("範例文字\n")
file.write("Hello File\n安an") #操作
# file.close() #關閉

# #關閉檔案基本語法： 檔案物件.close()
with open("data2.txt",mode="w",encoding="utf-8") as file:
    file.write("test\n換")
#但假如是使用with的寫法，他就不需要寫close，因為它會自動關閉，是比較安全的寫法

#讀取檔案
with open("data3.txt",mode="w",encoding="utf-8") as file:
    file.write("讀取此段") #先寫進
with open("data3.txt",mode="r",encoding="utf-8") as file:
    data=file.read() #再讀取
print(data)

#如果我要把檔案中的數字資料，一行一行的讀取出來，並且計算總額 寫法如下
sum=0
with open("data4.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3") #先寫進
with open("data4.txt",mode="r",encoding="utf-8") as file:
    for line in file: #一行一行的讀取
        sum+=int(line)
print(sum)


#使用json格式讀取、複寫檔案
#因為這個json讀取的資料是字典，所以寫法就要是字典的模式
import json
with open("config.json", mode="r") as file2:
    data=json.load(file2)
print(data) #data是一個字典資料
print("name:",data["name"])
print("version",data["version"]) 
data["name"]="New_w_w name" #修改變數中的資料
#把最新的資料複寫回檔案中
with open("config.json", mode="w") as file2:
    json.dump(data, file2)

# import json
# # file1=open("config.json", mode="r")  #想問，json不能用這種方式寫嗎？
# json.load()
# print(json)
# #想問這樣寫錯誤在哪？ 我以為他會執行json裡面的東西然後print出來，但看起來好像沒有 看不懂錯誤的意思