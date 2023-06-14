import random
users=random.randint(2,11) #users為自己,自己一開始遵造21點規則先取1個數值
npc=random.randint(2,11) #npc為莊家,莊家也是先取一個值
print("你的一開始的數字為:",users) #這裡先開牌(值),把一開始的users,也就是自己第一個值亮出來,npc莊家則不能亮讓大家知道
z=True #設一個布林數,先為True,待會會問你users要不要做+值動作,而此布林數是丟入while循環運作
summ=0 #summ用來做+值(users的)
npcsumm=0 #npcsumm用來做+值的(npc的)
n=1
while z : #這邊為主軸,進行21點加或不加值地方,當z為False,while就可以不用跑了
    answer=str(input("是否加值(YES/NO):")) #輸入YES or NO 是否+值
    if answer=="YES" or answer=="NO" : #YES為要+值 NO為不+值
        if answer=="YES" : #YES的話就進入
            n+=1   #n先+1,算次數
            if n==2 : #次數如果是2就進入
                summ=random.randint(2,11) #users做第2次亂數產生
                users+=summ #第2次亂數產生的值在跟users一開始的值+起來
                print(users,"提醒:你已經第",n,"次加值動作") #先列印你目前的值跟次數提醒
                npcno2=random.randint(2,11) #按照規則第2次users要+值npc也要跟著加值npcno2就是只有第2次亂數產生
                npc+=npcno2 #第2次亂數產生的值+npc一開始的值
            else : #次數n如果是大於2(不包刮2)就進去
                summ=random.randint(2,11) #summ做第n次亂數產生
                users+=summ #把第n次亂數產生的值在跟目前users的數值+起來
                print(users,"提醒:你已經第",n,"次加值動作") #之後先列印你目前的+起來的值跟次數提醒
                npc01=random.randint(0,1) #npc01是每次users要加值,npc會決定是否跟著加值,0為不加 1為跟著加值
                print("npc加值動作是",npc01) #顯示npc01是否+值 
                if npc01==1 : #npc01是1代表就是要+
                   npcsumm=random.randint(2,11) #npc也跟著亂數產生一個值
                   npc+=npcsumm     #把npc亂數產生的值+npc之前所有總和數值
            z=True #answer=="YES"部份好了之後每次來到這邊就是把布林數z用True等下循環 <-以防萬一的操作   
            if users==21 or npc==21 : #然後來到這如果users是21點就是為users贏家 或 npc是21點則為npc贏家
               if users==21 and npc==21 : #一開始如果兩者都21代表平局
                   print("雙方+值都21點,所以平局")
                   print("npc ",npc) #確認npc是否為21點
                   z=False #都21代表平局,while不用在循環
               elif users==21 :
                   print("你直接21點你贏了")
                   print("npc ",npc) #確認npc點數
                   z=False #你已經剛好滿點21點,所以你贏了,遊戲結束,所以while不用在循環了
               elif npc==21 :
                   print(npc,"npc已經21點 npc獲勝")
                   print("users ",users) #確認users(自己)點數
                   z=False #npc已經剛好滿點21點,所以npc贏了,遊戲結束,所以while不用在循環了
            elif users>21 or npc>21 : #users超過21點代表你輸了,就進去 或者npc>21代表他輸了 也進去
               if users>21 and npc>21 : #都超過21點代表平局
                   print("都超過21點,所以平局")
                   print("npc ",npc) #顯示npc超過21點的點數為多少
                   z=False #超過21點代表平局,while不用在循環了
               elif users>21 :
                   print("你輸了,超過21點")
                   print("npc ",npc) #確認npc的點數
                   z=False #超過21點已經遊戲結束,所以while不用再循環了
               elif npc>21 : #npc超過21點代表他輸了
                   print(npc,"npc超過21點,你贏了")
                   print("users",users) #確認users(自己)的點數
                   z=False
        elif answer=="NO" : #no就是不加值,所以選擇no就進去
            z=False #選擇不加值布林數z可以用False不用讓他循環了
    else :    
        print("你輸入錯誤,請選擇要YES(加值)或NO(不加值)")
if users<21 and npc<21 : #如果來到這邊代表while OK你也不加值了,然後如果你的users和npc不是==21 或是>21就近來這邊比大小
    if users>npc : #users大於npc進入,代表你贏了
        print("users->",users)
        print("npc->",npc)
        print("你贏了")
    elif users<npc : #users小於npc進入,代表你輸了
        print("users->",users)
        print("npc->",npc)
        print("你輸了")
    elif users==npc : #users==npc進入,雖然平局,但平局還是算該玩家(users)勝利
        print("users->",users)
        print("npc->",npc)
        print("最終牌數總值相同,但你贏了")
           
 
#題目:自製簡易21點
#撲克牌由小至大為2 3 4 5 6 7 8 9 10 J Q K都為10 A為11
#在這裡統一顯示出來
#然後這邊有改規則,就是一開始21點規定前2次必須要+牌值,之後才能選擇要"YES"還是"NO",但是在
#這邊把這個規則改掉!所以有做這個規則的修改
#加值意思->如果第2次要加值npc也會跟著+值,如果第3次要加值npc可選擇要+或不+
#補充如下:
#npc01意思->npc01亂數出來的0代表npc不要+值 1代表npc要+值


#範例如下:
#你的一開始的數字為: 10            你的一開始的數字為: 11       你的一開始的數字為: 3
#是否加值(YES/NO):YES             是否加值(YES/NO):NO         是否加值(YES/NO):YES
#12 提醒:你已經第 2 次加值動作     users-> 11                 7 提醒:你已經第 2 次加值動作
#是否加值(YES/NO):YES             npc-> 7                    是否加值(YES/NO):YES
#20 提醒:你已經第 3 次加值動作     你贏了                     17 提醒:你已經第 3 次加值動作
#npc加值動作是 1                                             npc加值動作是 0
#25 npc超過21點,你贏了                                       是否加值(YES/NO):YES
#users 20                                                   28 提醒:你已經第 4 次加值動作
#                                                           npc加值動作1
#                                                           都超過21點,所以平局
#                                                           npc 22    