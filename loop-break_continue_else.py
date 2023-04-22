#break
# n=0
# while n<5:
#     if n==3: #== 判斷的意思
#         break
#     print(n) #印出迴圈中的n
#     n+=1
# print("最後的n為",n) #印出迴圈結束後的n

#continue
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: #是一個運算式 可以參考number,string；它是取餘數的意思，那加上後面的==0，整句的意思就是『x/2的餘數如果為0(整除)』
#         continue #整除了就會到continue這一行，回到[]繼續下一個數字，不會到print
#     print(x)
#     n+=1
# print("最後的n為",n) #印出迴圈結束後的n

#else
sum=0
for m in range(11): #分別把0~10(不含11)放到m裡，m超過10時，就會跳到else
    sum+=m #每丟一次就跑sum=m+sum
else:
   print(sum) #印出0+1+2+...+10的總和


#綜合範例：找出平方根
#輸入9 得到3
#輸入11 得到【沒有整數的平方根】

n=input("輸入一個整數: ")
n=int(n) #將user輸入的字串轉成整數
for i in range(n): #從0 ~ n-1
    if i*i==n:
        print("整數平方根",i)
        break #用break強制結束迴圈
else:
    print("沒有整數平方根")
#所以當使用者輸入某個數字時ex.7，那麼for迴圈就會將i一個一個帶入，從0~6開始尋找i*i剛好等於n(7)的值
#若有則pirint整數平方根並且結束迴圈；若無則直接跳到else走另外一個print

