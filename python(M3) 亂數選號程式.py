import random  #會用到亂數 先設random
long=int(input()) #設一個代碼值,並且變數名稱為long
random.seed(long)  #random這邊設一個seed函數,並把代碼值放進去seed()裡,seed詳情下方有說明
data=[]             #設一個data=[],這一維陣列是取6個亂數產生的值
for i in range(0,6,1) : #for i循環6次代表每循環1次取1個1到42的值到現在的i值位置給data[i]
    data+=[random.randint(1,42)]
    for j in range(0,i,1) : #然後這邊是把目前位於的data[i]亂數值去比較她這i值前面的亂數值找有沒有重覆
        if data[i]==data[j] :#如果現在的data[i]<-(目前此i位置)亂數值跟前面的亂數值比起來有重覆就進去
            data[i]=random.randint(1,42) #進去之後,因為現在這data[i](目前這i值已經有值,所以直接針對這i位置的值
a=len(data)  #<-用len找出這data陣列的亂數有幾個值            #做重新亂數產生取值,之後底標返回,內圈for j繼續比較到結束!
for k in range(0,a,1) :  #來到這邊代表我long 透過seed的方式,保持了我原來利用data[]產出6個的亂數值(不重覆)
    print(data[k],end=" ")  #之後for k就每循還1次取我目前的data一維陣列的值 1個1個列印出來
print() 


#補充(seed意思)->python的seed很像JAVA的setseed,seed()用於設定隨機數種子，一個特定的種子可以
#               產生一個特定的偽隨機序列，這個函數的主要目的，是讓你的模擬能夠可"重複出現"，
#               因為很多時候我們需要取隨機數，但這段代碼(我的long)再跑一次的時候，
#               結果就"不一樣"了，"如果需要重複出現同樣的模擬結果的話"，"就可以用seed()"
#
#補充2->data=[]這邊要用"random"取6個隨機亂數給long,因為當初long丟到random裡的seed,所以設
#      一個data=[],利用他用"random"去取6個隨機亂數值,並且用seed保持這6個隨機亂數值!之後每一個隨機亂
#      數值就會保存起來丟給seed()裡的long
#
#補充3->for j 這邊假設我現在i是3 那就是第4個值,這樣for j就先找前3個值,if(data[i]<-(目前第4個值)==data[j]<-(目前前第1再來2再來3))
#      一個一個對我現在第4個值看有沒有重複,假設有就進去if裡面,然後把目前的i值<-(第4個)值,再換一個亂數產生值,之後底標返回,
#      返回到for j再繼續比較,比較到內圈for j ok為止 

#補充4->JAVA跟python是不同的程式語言,所以亂數演算出來的值不太一樣 所以答案有可能不同
#輸入代碼值(long)23323456
#            A:30 29 18 4 2 41