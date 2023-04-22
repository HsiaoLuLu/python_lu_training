#要先定義函式，才能呼叫函式！！
#基本語法： def 函數名稱(參數名稱)
#ex. 定義一個印出Hello的函式
# def sHello():
#     print("Hello")
# sHello()  #呼叫上方定義的函式 


# #定義也可以印出任何訊息的函式 ex.
# def say(m):
#     print(m) #把參數的資料印出來，print裡面的東西要＝參數名稱
# say("Hihi!!!") #呼叫上面的函式，在每次呼叫時可以有彈性

# #定義一個可以做加法的函式，中間用逗號隔開 ex.
# def add(n1,n2):
#     result=n1+n2
#     print(result)
# add(5,7) #呼叫上方的函式，將數字帶回定義區塊的函式，且做運算並print出來
# add(6,9)


# # #定義函式
# # def numb():
# #     print(3*4) #若函式內部的程式碼只有被定義沒被呼叫的話，就不會執行！
# # #呼叫函式
# # numb() #呼叫時的寫法，定義的名稱+小括號

# #定義函式
# def numb(n1,n2):
#     print(n1*n2)
# #呼叫函式
# numb(6,6)
# numb(0,8)

#定義
from unittest import result


def list(n1,n2):
    print(n1+n2)
    return n1*n2
#呼叫
value=list(3,4)
print(value)


# 範例一：定義一個印出 hi 的函式
def hiAlvis():
    print("hi")
# 呼叫上方定義的函式
hiAlvis()

#範例二：
def 函式名稱(參數名稱):
    #函式內部的程式碼
    return 
# 在這裡，return 的用法是：結束函式，因為沒有定義資料，所以回傳 None，這裡的 None 我們稱為回傳值。
def 函式名稱(參數名稱):
    #函式內部的程式碼
    return #資料
# 在這裡，return 的用法是：結束函式，回傳「資料」，這裡的資料我們稱為回傳值。

# 函式回傳 None
def say(sth):
    print(sth)
    return
# 呼叫函式，取得回傳值(None)
value=say("hi alvis")
print(value) # 這裡我們會印出「None」
#這邊解析一下程式碼的運作流程：當我們呼叫函式「say(“hi alvis”)」，他會跳到上方的定義函式，上方的函式會定義參數 sth=”hi alvis” 然後順著程式走，印出「hi alvis」
# 這時遇到 return，會跳回到呼叫函式的區塊，然後回傳值的結果是 None（因為 return 我們沒有給資料，就是 None），所以「say(“hi alvis”)」函式結果就是 None，也就是回傳值的結果。
#接著 None 會放進我們定義的變數「value」裡，接著程式碼就會印出 value 的結果「None」。

# 函式回傳字串 Hi
def add(n1, n2):
    result=n1+n2
    return "Hey!"
# 呼叫函式，取得回傳值(Hi)
value=add(1, 8)
print(value) # 這裡我們會印出 Hi
#一樣先看下方呼叫函式的區塊，value=add(1, 8) 跳到上方訂的函數中，其中 n1=1、n2=8 順著上方區塊的程式碼走，把這個結果放進變數 result 中得到 9
# 運算完之後遇到 return，這裡的 return 告訴我們要回傳字串 “Hi”，所以 add(1, 8) 的結果就成了「”Hi”」放進變數 value 裡面，印出「Hi」。
#其中要注意的就是我們呼叫函數時，或定義函數中有 return，則函數回傳的結果就是看 return 的回傳值，跟原本的程式碼無關，所以不要混在一起
# 程式碼跑的結果歸程式碼跑的結果，回傳值歸回傳值，兩者是分開的。