#輸入兩個年份判斷兩個年份的總天數總值
n=int(input())   #輸入兩個年份 n 跟 m
m=int(input())
sum=0           #sum 待會要拿來算兩個年份之間的閏年總值
sum1=0          #sum1待會要拿來算兩個年份之間的非閏年總值
a=0            #閏年用
b=0           #非閏年用
for i in range(n,m+1,1) : #兩個年份丟入for循環
    if i%400==0 :  #如果我目前的i值是%400==0 那就是閏年
        a=366      #a做生成值->(366)
        sum=sum+a  #這時候用sum去加剛剛生成值的a值
    elif i%100==0 : #如果我目前的i值是%100==0 那就是非閏年
        b=365       #b做生成值->(365)
        sum1=sum1+b #這時候用sum1去加剛剛生成值的b值
    elif i%4==0 :   #如果我目前的i值是%4==0 那就是閏年
        a=366       #a做生成值->(366)
        sum=sum+a   #這時候sum去加剛剛生成值的a值
    else :     #else部分只要目前i值%400 %100 %4!=0(不等於0) 那就丟這
        b=365      #一樣這邊是非閏年,所以b做生成值->(365)
        sum1=sum1+b   #這時候用sum1去加被剛剛生成值的b值
print("總天數為: ",(sum+sum1)) #等到我for迴圈的兩個年份間判斷完再拉來這邊,  
                              #把總和閏年總值(sum)跟總和非閏年總值(sum1)加起來變成"總天數總值"
                              
#n->1616           n->1000             閏年可用if迴圈判斷,判斷年份時 判斷式的年份要
#m->1618           m->1400             從最高至最低放, %400 %100 %4 這樣,else是
#總天數為: 1096    總天數為: 146462     最後上面三個不符合再放的!
