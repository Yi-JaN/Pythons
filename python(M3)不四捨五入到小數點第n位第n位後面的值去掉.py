import math #插入數學公式 待會要呼叫floor
m=float(input()) #輸入一個浮點數
n=int(input()) #輸入一個n,此n做小數點第n位,然後他還有一個任務,就是丟到for迴圈當循環次數
summ=1 #summ先設為1,待會for迴圈每循還1次summ要*10一次
for i in range(1,n+1,1) : #n丟入for循環,從1開始 1<n+1 每循環1次+1
    summ*=10  #每循還1次*10,一開始從1開始乘
if summ>=10 : #如果summ>=10就丟入,而為什麼是>=10呢? 因為在floor裡10是小數點第1位 100是第2位,以此類推
    print(math.floor(m*summ)/summ) #floor是小數點第n位數後面的值去掉,不4捨5入
else : #其他<10就丟到else裡
    print(math.floor(m)) #floor這邊只列印該m值浮點數,這樣列印就是小數點第0位後面的值被去掉,不4捨5入
    
#題目:不四捨五入到小數點第n位第n位後面值去掉
#補充math.floor-> math.floor(m*summ)/summ,我在summ放10的話就是留到小數點第1位,後面值去掉,不4捨5入
#                 math.floor(m*summ)/summ,我在summ放100的話就是留到小數點第2位,後面值去掉,不4捨5入
#                 math.floor(m*summ)/summ,我在summ放1000的話就是留到小數點第3位,後面值去掉,不4捨5入,之後以此類推
#                 math.floor(m),意思是針對此m值,小數點第1位(包含第1位)後面值去掉,只留整數,不4捨5入
    
#輸入->21.689   3.14159    3.14159    1.88   16.6953    101.23547
#輸入->2        2          1          0      0          3
#輸出->21.68    3.14       3.1        1      16         101.235
    