#M3 數字拆解
n=int(input()) #輸入一個正整數
str1=""      #待會用str1,也就是字串取正整數
sum=0        #輸入一個總和,待會要加這正整數的和
if n==0 :    #如果n是0,就直接丟這
    sum=0    #總和跟str1就都是0
    str1=str(n) 
while n>=1 :   #如果是>=1,丟進去循環直到外圈審核不能再進
    sum=sum+n%10   #sum去加我1個1個%出來的總和n值
    str1=str(n%10)+str1 #這邊是取我目前的n的1個1個值轉成str,最後再丟給變數名稱str1做生成值
    n=n//10            #sum跟str1剛剛做生成值OK之後來到這邊,目前的n//10,出來的值,丟回While做外圈審核
print("總和為: ",sum)    #While循環到OK之後往下來到這邊,先列印總和值
m=len(str1)        #接著在把str1最終拿到的數字字串值丟給len,看有幾個單字串
for i in range(0,m,1) : #之後用for,i=0 從0開始到<m ,0<m,1次+1, 類似於JAVA裡的str.length
    ch=chr(ord(str1[i]))  #ch去汰舊換新後面出來的值,由內到外,先取str1目前的i值單字串,再轉成ord變ASCII,
    print(ch,end=" ")    #變ASCII後再轉chr變成單字串,之後丟給ch做生成值,往下print列印單字串,以此類推到for循環結束
print()       #forOK之後,最後來到這邊做換行字元!


#(1.) n->1289173
#總和為: 31
#1 2 8 9 1 7 3
#(2.) n->015
#總和為: 6
#1 5
#(3.) n->0
#總和為: 0
#0  