#取3個字串值判斷是否迴文 (先用一維陣列取3個字串值)
m=int(input())  #輸入m組資料型態
str1=[]         #這邊先用str1一維陣列取我的字串
for i in range (0,m,1) : #資料型態丟進去 取0<m 組字串,str1一個一個自己輸入,在自己轉str丟給自己str1
    str1+=[str(input())]  
for j in range(0,m,1) :  #資料型態丟進去 用str3去接我目前str1一維陣列位於的[j]值字串
    str3=str1[j]   #str3做生成值
    str2=""      #輸入一個str2待會反向取單字串用
    a=len(str3)   #算目前取的str3的字串長度
    for k in range(a-1,-1,-1) : #str開頭第1個單字串必為0 ,所以反向取值
        ch=chr(ord(str3[k])) #ch生成值-> 由內到外(從ord到chr),目前取到的str3把他的str3[k]位於的單字串k值先轉ord轉好後再轉chr單字串 最後給ch做生成值
        str2+=ch           #之後再丟給str2慢慢一個一個單字串加起來 
    if str3==str2 :   #如果現在的str3的字串跟str2反向單字串一個一個加起來的字串值是一樣的話就符合
        print(str3,end=" ")  #符合就列印現在這個字串,之後空格,有加end就不換行,然後就這樣for迴圈一直循環到OK之後
print()         #OK之後往下來到這邊換行字元


#補充:每str3的生成值拿到的新字串 就會由上至下 把前一個OK好的舊字串的東西做換掉變剛剛生成值的新字串的東西
#     畢竟接下來是要找新字串是否迴文
#3                        5
#12321                     12321    A:12321 AbcbA #bc cb#
#124321                    124321 
#!vC# #Cv!                 AbcbA
# A: 12321 !vC# #Cv!       #bc cB#
#                          #bc cb# 