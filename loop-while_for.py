#while迴圈
# n=1
# while True:#如果用True,會形成無窮迴圈，因為永遠都是True
#     print(n)
#     n+=1

# n=1
# while n<=10:
#     print(n)
#     n+=1

# n=1
# sum=0 #記錄累加的結果
# while n<=10:
#     sum=sum+n
#     n+=1
#     print(sum) #縮排有差，會影響到整個結果，如果print與while裡面的迴圈同一排，則每跑一次迴圈，sum就會印出一次sum=sum+1

# n=1
# sum=0 #記錄累加的結果
# while n<=10:
#     sum=sum+n
#     n+=1
# print(sum) #縮排有差，會影響到整個結果，如果print與while迴圈同一排，則最後的sum就會印出累加後的結果，而不會單筆逐一列出


#for迴圈
#基本語法會使用到for和in  ex.for變數名稱in列表或字串：將列表中的項目或字串中的字元逐一取出，逐一處理
# for x in [3,5,1]:
#     print(x)  #代表x會分別把3,5,1印出來

# for x in "Can":
#     print(x)  #代表x會分別把Can印出來

for x in range(5):
    print(x)  #range代表0~4的列表(記得從0開始不包含尾數5)

# for x in range(5,10):
#     print(x)  #range代表5~9的列表，因為他已經有給你頭尾的區間，所以就不是從0開始而是從5開始(一樣不包含尾數10)

#累加除了用while迴圈，也能使用for迴圈
#1+2+3+4....+10 可以用以下for迴圈進行
add=0
for x in range(11):
    add=add+x
print(add)