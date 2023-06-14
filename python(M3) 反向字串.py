str1=str(input())  #輸入一組字串
str2=""      #待會反向字串1個1個+用的
n=len(str1)  #取我str1的len,看單字串長度多少
for i in range(n-1,-1,-1) : #把單字串長度丟進去,那因為是反向字串,從後到前,str開頭要0,所以這邊就n-1跟-1 變成, n-1>-1 ,1次+(-1)
    ch=chr(ord(str1[i]))  #ch去汰舊換新我的單字串值,由內到外,先取我str1位於的目前i值單字串,之後取到單字串轉成ord變單字串
    str2+=ch              #ASCII碼,變ASCII碼後再轉chr,ASCII碼轉單chr值,之後往前丟給ch做生成值,  之後往下丟給str2去加單字串
print(str2)     #以此類推循環到最後for循環OK之後,把我str2裡的1個1個單字串組合起來的值列印出來!


# str1->Avc123     str1->#BcV !12w     str開頭要為0,反向字串就像上面一樣n-1 之後再-1 變成 n-1>-1 1次+(-1)循環for
# A:321cvA          A:w21! VcB#