#4/4 read
#數字運算

A=3+6
print("A",A) 
B=3*6
print("B",B)
#除法分成整數除法和小數除法，小數除法/，整數除法//(不會除到小數點)
C=5/20 #小數除法(除多少算多少，可以想像成一般我們的除法)
print("C",C)
D=7//6 #整數除法(只取到整數，不會取到小數點，也沒有四捨五入的狀況)
print("D",D)
Ee=2**3 #次方
print("Ee",Ee) 
F=2**0.5 #開根號
print("F",F)
G=8%3 #取餘數
print("G",G)
H=2+3
H+=1 #(左邊算式其實為H=H+1，會把先有的變數，再做更新；除了加法之外其餘的"減,乘,除"皆能使用)
print("H",H)
I=3*3
I-=2 #他其實就等於I=I-2
print("I",I)
J=2*2
J*=5 #等於J=J*5
print("J",J)

#字串運算
K="Hihi" #字串建立單雙引號都可以
print("K",K)
L="How\"s" #如果在引號前面打斜線\，則會跳脫和外面的引號做區隔，裡面的雙引號就會顯示在字串中
print("L",L)
M="Thank"+"Youu" #把兩個字串串起來做連接(如果不要用+，也可以直接空ㄧ格，也一樣會和+有相同效果)
print("M",M)  
N="Hello\n你好" #\n代表換行的意思
print("N",N)
O='''Hello 

And Hi'''  #和上面的\n是一樣的意思，都是換行的意思(可以寫多行文字)，但記住一定要三個"or三個'，不能混搭。如果是使用此方式，就可以直接Enter換行(如左範例)
print("O",O)

P='caffee'*3 #在字串後面用*n，代表會重複此文字n次
print("P",P)

#字串會對內部的字元做編號(索引)，從0開始算起(不是1喔！)
Q="number"
print("Q",Q[3]) #類似取陣列的概念，從0開始找，n=0，以此類推，所以3=b
R="number"
print("R",R[1:3]) #取一串特定範圍的字元，從1~3的字元，包含開頭編號，但不包含結尾編號
S='number'
print("S",S[2:]) #如果只給開頭沒給結尾，那他print出來的就會是從你設定的起始到最後的所有字元
T='number'
print("T",T[:3]) #如果只給結尾沒給開頭，那他print出來的就會是從頭(0)到你結尾設定的字元(但記得不包含結尾編號)；所以範例T所print出來的範圍會是[0,1,2]這三個字串
