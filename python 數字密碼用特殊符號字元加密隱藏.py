import random
str1=str(input()) #依照下方題目輸入所說,輸入值轉str
str2="" #設一個空白字串,待會要拿來用最終數字的特殊符號字元加密
print("你輸入的密碼為: ",str1) #先列印你剛剛輸入的密碼值
data=[] #依照下方題目輸入所說,輸入值轉str後用"陣列"取4位數的值,所以data是一個一維陣列
for o in range(0,4,1) : #for o是負責取我str1的單字串然後丟進去給data一維陣列裡
    ch=str1[o]         #第一個單字串的位置值和陣列第一個值都為0,所以從0開始,每循環1次+1
    data+=[ch]
for i in range(0,4,1) : #來到這邊,for i負責取data一維陣列i位置值的單字串,陣列第一個位置值為0,從0開始,每循環1次+1
    alls=data[i] #每循環第一步先取data一維陣列的i位置值的單字串給alls做生成值
    allstwo=int(alls) #然後依照題目敘述去判斷該單字串轉int值是0還是奇數還是偶數,所以這行就是把目前的單字串轉int值給allstwo
    if allstwo==0 : #如果單字串轉int是0就進去
        ch0=random.randint(1,3) #進去後先亂數產生1到3,等等要用0的亂數特殊符號字元
        print(ch0,end=" ") #然後把產生到的1到3看是哪個值顯現出來,然後再空格
        if ch0==1 : #如果亂數是1
            str2+="#" #str2就+"#"
        elif ch0==2 : #如果亂數是2
            str2+="~" #str2就+"~"
        elif ch0==3 : #如果亂數是3
            str2+="-" #str2就+"-"
    elif allstwo%2>0 : #如果單字串轉int是奇數就進去
        ch1=random.randint(1,3) #然後先亂數產生1到3,等等要用奇數的亂數特殊符號字元
        print(ch1,end=" ") #然後把產生到的1到3看是哪個值顯現出來,然後再空格
        if ch1==1 : #如果亂數是1
            str2+="*" #str2就+"*"
        elif ch1==2 : #如果亂數是2
            str2+="+" #str2就+"+"
        elif ch1==3 : #如果亂數是3
            str2+="!" #str2就+"!"
    elif allstwo%2==0 : #如果單字串轉int是偶數就進去
        ch2=random.randint(1,3) #然後先亂數產生1到3,等等要用偶數的亂數特殊符號字元
        print(ch2,end=" ") #然後把產生的1到3看是哪個值顯現出來,然後再空格
        if ch2==1 : #如果亂數是1
            str2+="@" #str2就+"@"
        elif ch2==2 : #如果亂數是2
            str2+="$" #str2就+"$"
        elif ch2==3 : #如果亂數是3
            str2+="/" #str2就+"/"
print() #for i ok之後來到這邊先換下一行
print("你的最終數字加密為: ",str2) #之後列印我最終數字的特殊符號字元加密
        
#題目敘述:4位數的數字密碼用特殊符號字元加密隱藏
#如果是0->亂數產生1到3->1為# 2為~ 3為-
#如果是奇數->亂數產生1到3->1為* 2為+ 3為!
#如果是偶數->亂數產生1到3->1為@ 2為$ 3為/

#題目輸入:限定1.輸入值轉str然後用陣列取4位數的值

#輸入->3214                     0319                        2506
#你輸入的密碼為: 3214           你輸入的密碼為: 0319         你輸入的密碼為: 2506
#1 2 1 1                       2 3 3 2                      1 3 3 1
#你的最終數字加密為: *$*@       你的最終數字加密為: ~!!+      你的最終數字加密為: @!-@