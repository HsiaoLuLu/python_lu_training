#無限參數
# def 函式名稱(*無限參數): #()內用*號
#     #無限參數以Tuple資料型態處理函式內部的程式碼(tuple=有序列表)
# #呼叫函式，可傳入無限數量的參數
# 函式名稱(data1,data2,data3) #()可以無限延伸

# #參數預設資料
# def power(aaa,bbb=0): #如果第二個沒給參數，需要給一個預設的參數，不然會error
#     print(aaa**bbb) #一個*是乘法，兩個*是平方
# power(3,2)
# power(4) #只給aaa沒給bbb，故bbb就會取上面一開始提供的預設數


# #使用參數名稱對應
# def num(n1,n2):
#     print(n1/n2)
# num(2,4)
# num(n2=2,n1=4) #這就是特別有指定n2和n1是哪個數字，就不用管位置了

#無限/不定 參數資料

# def avg(*ns):
#     print(ns)
# avg(3,4)
# avg(3,5,10)
# avg(1,4,-1,-8)


def summ(*ns):
    sum=0
    for n in ns:
        # print(n)
        sum=sum+n
    print(sum/len(ns))
summ(3,4)
summ(3,5,10)
summ(1,4,-1,-8)