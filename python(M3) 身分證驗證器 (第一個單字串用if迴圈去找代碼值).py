#身分證驗證器 (第一個單字串用if迴圈找代碼值)
str1=str(input())  #我輸入一組字串(身分證)
ch=str1[0]    #讓ch拿到我str1這組字串的第一個單字串
sum=0    #設一個sum=0 ,待會找第一個單字串的代碼值用
if ch=='A' : #ch拿到第一個單字串的值之後,接下來找他的代碼值,用if迴圈找,看位於哪裡
  sum=10     #找到位於的點,裡面的sum就是這第一個單字串的代碼值
elif ch=='B' :   
   sum=11
elif ch=='C' :     #題目的第一個單字串位於代碼值的表格
   sum=12          #第一頁
elif ch=='D' :     #單字串-> A   B   C   D   E   F   G   H   J   K   L   M
    sum=13         #代碼值-> 10  11  12  13  14  15  16  17  18  19  20  21
elif ch=='E' :     #第二頁
    sum=14         #單字串-> N   P   Q   R   S   T   U   V   X   Y   W   Z
elif ch=='F' :     #代碼值-> 22  23  24  25  26  27  28  29  30  31  32  33
    sum=15         #第三頁
elif ch=='G' :     #單字串-> I   O
    sum=16         #代碼值-> 34  35
elif ch=='H' :
    sum=17
elif ch=='J' :
    sum=18
elif ch=='K' :
    sum=19
elif ch=='L' :
    sum=20
elif ch=='M' :
    sum=21
elif ch=='N' :
    sum=22
elif ch=='P' :
    sum=23
elif ch=='Q' :
    sum=24
elif ch=='R' :
    sum=25
elif ch=='S' :
    sum=26
elif ch=='T' :
    sum=27
elif ch=='U' :
    sum=28
elif ch=='V' :
    sum=29
elif ch=='X' :
    sum=30
elif ch=='Y' :
    sum=31
elif ch=='W' :
    sum=32
elif ch=='Z' :
    sum=33
elif ch=='I' :
    sum=34
elif ch=='O' :
    sum=35 
v1=sum//10  #把第一個單字串找到的代碼值取十位數給v1
v2=sum%10   #把第一個單字串找到的代碼值取個位數給v2
all=v1+(9*v2) #all為整個字串(身分證)的代碼總值 那一開始先加第一個單字串代碼值  第一個單字串公式-> v1+(9*v2)
k=8   #k設8,因為待會要從第2個單字串開始取代碼值,8就跟第2個單字串乘 7就跟第3個單字串乘 以此類推 k變1時 算到後面的值就用1去乘
a=len(str1) #算str1(身分證)的總長度
for i in range(1,a,1) : #for從1開始,代表從第2單字串開始到結束 1<a 1次+1
    c=int(str1[i])  #身分證從第2碼開始為數字字串,所以把數字字串1個1個取過來轉int再給c生成值,注意:轉int限數字字串
    all=all+(k*c)   #all就一直加,加到for循環結束
    if k > 1 :      #如果k>1 就進去k減1 如果k已經是1 就跳過此if迴圈,往下再返回for迴圈  
       k-=1
if all%10==0 and ch>='A' and ch<='Z':   #來到這邊就代表for迴圈循環完畢,all也拿到這組str1(身分證)的代碼總值
   print("CORRECT!!!")  #如果all%10==0 就代表這身分證正確 顯示 "CORRECT!!!"
elif all%10!=0 :      #其他如果all%10!=0 取餘數不等於0 代表這身分證是錯的 顯示"WRONG!!!"
   print("WRONG!!!")

#題目詳請去模三題目 身分證驗證器去看        
#  A123456789   L163690274   C123456889
#A:CORRECT!!! A:WRONG!!!   A:CORRECT!!!