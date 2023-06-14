import random
z=True
while z : #z如果是True,該while繼續循環,如果是False,該while就停止循環
    abc="ABCDEFGHJKLMNPQRSTUVXYWZIO" #abc為一組字串,此字串是依照身份證第一個碼做設定,每循環1次就為該字串
    number="0123456789" #number為一組字串,此字串是依照身份證接下來第3到第10個碼做設定,每循環1次就為該字串
    number12="12" #number12為一組字串,此字串是依照身分證第2個碼做取值動作,第2個碼1為男生,2為女生,每循環1次就為該字串
    str1="" #此空字串是待會要拿來放設定好的身份証,每循環1次為空字串
    summ=0 #此summ是待會要取身份証第一個碼的代號數字,每循環1次歸0
    alls=0 #此alls是待會身份證每個碼的代碼總和,每循環1次歸0
    ch=random.choice(abc) #ch先負責取choice隨機產生abc裡的單字串,然後此單字串是身份証第一個碼
    if ch=="A" : #取到的第一碼依照下方注意1去取代號
      summ=10
    elif ch=="B" :
        summ=11
    elif ch=="C" :
        summ=12
    elif ch=="D" :
        summ=13
    elif ch=="E" :
        summ=14
    elif ch=="F" :
        summ=15
    elif ch=="G" :
        summ=16
    elif ch=="H" :
        summ=17
    elif ch=="J" :
        summ=18
    elif ch=="K" :
        summ=19
    elif ch=="L" :
        summ=20
    elif ch=="M" :
        summ=21
    elif ch=="N" :
        summ=22
    elif ch=="P" :
        summ=23
    elif ch=="Q" :
        summ=24
    elif ch=="R" :
        summ=25
    elif ch=="S" :
        summ=26
    elif ch=="T" :
        summ=27
    elif ch=="U" :
        summ=28
    elif ch=="V" :
        summ=29
    elif ch=="X" :
        summ=30
    elif ch=="Y" :
        summ=31
    elif ch=="W" :
        summ=32
    elif ch=="Z" :
        summ=33
    elif ch=="I" :
        summ=34
    elif ch=="O" :
        summ=35
    one1=summ//10 #one1為summ(第一個代碼)除以10取商數值,也就是取類似十位數的值
    one2=summ%10  #one2為summ(第一個代碼)除以10取餘數值,也就是取類似個位數的值
    alls=one1+(9*one2) #alls這時候為one1+(9*one2),也就是第一碼成功完畢
    k=8 #這時候設k=8,也就是待會要重第2個碼-第10個碼做取代碼動作
    str1+=ch #str1這時候可以+身份證第一個碼
    for i1 in range(0,1,1) : #for i1從0開始,然後0<1,每循環1次+1,循環1次,此for i1取身分證第2個碼
        str1+=random.choice(number12) #每循環1次str1就加用choice生成出來的(number12)單字串
    for i in range(0,8,1) : #for i從0開始,然後0<8,每循環1次+1,循環8次
        str1+=random.choice(number) #每循環1次str1就加用choice生成出來的(number)單字串
    for j in range(1,10,1) : #for j從1開始,然後1<10,每循環1次+1,循環9次
        chint=int(str1[j]) #每循還1次chint就生成值為str1目前j位置值的單字串轉int值
        alls+=k*chint #alls就+目前k*chint的值,一點一滴慢慢依照for j總合起來
        if k>1 : #循環下來如果k是大於1,那就進去
          k=k-1 #進去取我符合該if k>1 :的k,然後做k=k-1
    if alls%10==0 : #然後來到這邊我的alls除以10取餘數是0的話,那就代表是ok的
       print("此隨機產生身份證: "+str1)
       z=False #因為是ok的,那z就變布林代數的False(否)
        
            
#注意1:身份證第一個碼的代號如下
# A   B   C    D    E    F    G    H    J    K    L    M    N    P    Q     R
#10  11  12   13   14   15   16   17   18   19   20   21   22   23   24    25             
# S   T   U    V    X    Y    W    Z    I    O
#26  27  28   29   30   31   32   33   34   35

#範例答案如下:
#此隨機產生身份證: R276150347            此隨機產生身份證: E130289078 