#4/4 read
#集合的運算 用大括號{}
# s1={3,4,5}
# print(8 in s1) #可以用in來判斷前面的數字是否有在s1中，會印出True或False
# print(8 not in s1) #與前行差異在，在in前加了not就變成相反的意思，判斷前面的數字是不是沒有在s1中，會印出True或False

# s1={3,4,5}
# s2={4,5,6,7}
# #s3=s1&s2 #若要取兩個set中交集的數字，會用&做銜接 & ->交集
#print(s3)

# s3=s1|s2 #若要取兩個set中的所有資料且不重複，會用|做銜接 | ->聯集
# print(s3)

#s3=s1-s2 #從s1中，減去s2重疊的部分，會用-做銜接(記得s1和s2位置順序顛倒的話，他們的意思也會不一樣) - ->差集
#print(s3)
#s3=s2-s1
#print(s3)

#s3=s1^s2 #取兩個集合中，所有不重疊的部分，會用^做銜接 ＾-> 反交集
#print(s3)

# s=set("lesson") #set(字串)，把字串中的字母拆解成集合
# print(s) #print出來的集合，字母會是隨機的
# print("H" in s) #測試看看H有沒有在s的集合裡，會回傳True或False


# 字典的運算 大括號，Key:value的配對(用冒號)，配對與配對間用逗號隔開
# dict={"apple":"蘋果","banana":"香蕉"}
# print(dict["apple"])

# dict={"apple":"蘋果","banana":"香蕉"}
# print("apple" in dict) #判斷Key是否存在，他不會判斷value，會回傳True或False

#dict={"apple":"蘋果","banana":"香蕉"}
#print("dumpling" in dict) #判斷Key是否存在，他不會判斷value，會回傳True或False

# dict={"apple":"蘋果","banana":"香蕉"}
# print("dumpling" not in dict) #判斷Key是否存在，他不會判斷value，會回傳True或False

# dict={"apple":"蘋果","banana":"香蕉"}
# print(dict)
# del dict["banana"] #刪除字典中的鍵值對(key:value pair)
# print(dict) #這一個print後的值，就會是刪除banana這個鍵值後的值

dic={x:x*3 for x in [2,3,4]} #以列表中的資料當基礎產生字典，固定用for和in，把列表[]內的項目轉換成鍵值對
print(dic) #列印出來的值就會是[x:x*3,x:x*4,x:x*5]
