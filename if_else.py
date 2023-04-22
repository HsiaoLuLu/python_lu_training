#4/5 read
#if else 判斷式
#if True:
#    print("True 執行")

# A=1
# print(A)
# print("A:",type(A))
#小數點會得出float，整數會得出int

# x=input("請輸入數字: ") #取得字串形式的使用者輸入
# x=int(x) #將字串型態轉為數字型態
# if x>200:
#     print("大於200")
# elif x>100:
#     print("大於100,小於等於200")
# else:
#     print("小於等於100")
#上面的三個結構會是一起的，也只會執行其中一個運算式，執行完就會跳出


#四則運算1
# n1=int(input("請輸入數字一："))
# n2=int(input("請輸入數字二："))
# print(n1*n2) #會把n1和n2做運算，+-*/都可以用

#四則運算2
# = 是賦予的意思，ex.a=1，意思是把1賦予到a上面
# == 是等於的意思，通常用來判斷是否相等，大多出現在判斷裡
n1=int(input("請輸入數字一："))
n2=int(input("請輸入數字二："))
op=input("請輸入運算：+,-,*,/：") #使用者可以決定他要做哪個運算
if op=="+":
    print(n1+n2) #+成立，就會跑這個
elif op=="-":
    print(n1-n2) #-成立，就會跑這個
elif op=="*":
    print(n1*n2) #*成立，就會跑這個
elif op=="/":
    print(n1/n2) #/成立，就會跑這個
else:
    print("無法判斷") #+-*/都不是就會跑這個
