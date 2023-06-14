str1=str(input())  #輸入一組字元
str2=""            #用str2並且是空的 待會接我str1反向的一個一個的單字串 
n=len(str1)       #先測str1這字串長度 類似於JAVA的str.length
for i in range(n-1,-1,-1) : #把測出來的長度丟進去,n-1是因為 str第一個單字串必為0,所以n-1然後-1 -> n-1>-1 每次+(-1)
    ch=chr(ord(str1[i]))   #ch做生成值 由內到外先從str1[i](i位於的單字串)轉成ord變ASCII碼,之後變ASCII後再轉單字串chr,之後丟給ch
    str2+=ch        #丟給ch生成值後就丟到下方交給str2去加單字串,以此類推 到for迴圈循環結束!
if str1==str2 :    #OK後來到這邊然後比較我現在的str1跟str2一樣的話丟進來顯示YES
    print("YES")
elif str1!=str2 :  #不一樣來到這邊(elif)顯示為"NO"
    print("NO")    



#str1->12321    str1->#vC! !Cv#
#    A:YES           A:YES
#str1->124321   str2->#vC !Cv# 
#    A:NO            A:NO