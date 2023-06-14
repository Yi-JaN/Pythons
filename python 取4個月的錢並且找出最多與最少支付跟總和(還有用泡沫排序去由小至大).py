#取4個月的支出(找出最高與最少支出跟總和)(還有用泡沫排序由小至大)
money=[] #用一維陣列取4個月的錢
for i in range(0,1,1) :  #題目固定說取4個月,所以這邊我每取一份的錢為1個月
    money+=[int(input("請輸入第 1 個月份的支付金額: "))]
for i1 in range(0,1,1) : #1個月取完換取第2個月
    money+=[int(input("請輸入第 2 個月份的支付金額: "))]
for i2 in range(0,1,1) : #第2個月取完換取第3個月
    money+=[int(input("請輸入第 3 個月份的支付金額: "))]
for i3 in range(0,1,1) : #第3個月取完換取第4個月
    money+=[int(input("請輸入第 4 個月份的支付金額: "))]
m=len(money)  #取出4個月的錢之後,列出一維陣列的長度
maxx=0   #這邊開始找4個月裡的最多跟最少支出,maxx為最多,minn為最少
minn=0
for j in range(0,m-(m-1),1) : #先固定取第1個值為maxx跟minn,怕集中一個for取會出差錯
    maxx=money[j]            #所以統一第1個值先跟其他值分開用其他各自for去算
    minn=money[j]           #怕第一個值集中1個for算會亂跑maxx或minn,所以分開成2個for
for k in range(1,m,1) :   #這邊是第2個值開始,那因為陣列第1個值必為0,所以第2個值從1開始循環
    if money[k]>maxx :    #然後if這邊把maxx跟minn已經是第1個值得值丟進去判斷,從第2個值循環
        maxx=money[k]     #然後一直循環符合就maxx或minn各自做生成值,跑到這迴圈ok,最後的maxx跟minn就為最終最大跟最小!
    elif money[k]<minn :
        minn=money[k]
summ=0        #取出最大跟最小後,這邊開始為算這4個月的錢
for x in range(0,m,1) : #每循環一次,summ就加money目前取的[x]位置的值去+,循環結束就代表總和OK
    summ+=money[x]        
for a in range(0,m,1) : #這裡開始用泡沫排序法,泡沫排序法詳請請去python資料夾/M3/python(M3)泡沫排序(氣泡排序)
    for b in range(0,m-1,1) :  #(由小到大)(也有由大至小說明) <-開這個檔案去看說明
        if money[b]>money[b+1] :#由小到大是money[b]>money[b+1] 由大至小是money[b]<money[b+1]
            v=money[b]
            money[b]=money[b+1]
            money[b+1]=v
print("支付最多的金額為: ",maxx) #來到這邊最多列出來
print("支付最少的金額為: ",minn) #來到這邊最少列出來
print("支付的總和為: ",summ)     #來到這邊總和列出來
print("支付金額由小到大排序為: ",money)  #來到這邊已經經過泡沫排序法的循環已經把money一維陣列的值
                                       #變成最完美狀態的由小到大的money一維陣列
                                       #所以這邊列出money從第一個到最後的一維陣列全部值列印出來

#題目範例:
#請輸入第 1 個月份的支付金額: 25000
#請輸入第 2 個月份的支付金額: 34000
#請輸入第 3 個月份的支付金額: 30000
#請輸入第 4 個月份的支付金額: 18000
#A:
#支付最多的金額為: 34000
#支付最少的金額為: 18000
#支付的總和為: 107000
#支付金額由小到大排序為: [18000, 25000, 30000, 34000]                                   