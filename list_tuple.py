#4/4 read
#List 有序可變動列表，使用中括號[]
# grades=[80,66,54,98,100]
# print(grades[3]) #列表索引，選取指定的位置
# grades[2]=77 #把77放到列表中編號2(第三個)位置
# print(grades)
# print(grades[0:2]) #取列表中編號0~2的位置(不包含2，去尾)

# grades[1:3]=[]  #代表將指定數值刪除的意思，原先編號1~3位置(不包含3，去尾)裡面的數值會被刪掉
# print(grades)

#列表也可以做簡單的串接 ex.
#grades=grades+[87,92,47] 
#print(grades)

#取得列表長度，使用len；也可以先設定用length作替代，到時候print就只要寫length就行
# print(len(列表))
# print(len(grades))

# length=(len(grades))
# print(length)

#巢狀列表
# data=[[3,4,5],[6,7,8]]
# print(data[1][2]) #第一個[]代表是第n組大list，第二個[]則代表為該list裡面編號哪個數字

#Tuple 有序不可變動列表，都是小括號()
data=(3,4,5)
#print(data[0:2])
data[0]=8 #和List差別在，Tuple裡的資料不可以變動！！
print(data)
