#遞迴函數: 數字拆解  #python遞迴建議從遞迴函數結尾下方由下至上循環
def answer(n,str1) : #把下方的數丟上來遞迴裡
    if n==0 :       #如果n是0進入
      if str1!="" :    #進入後假設剛剛有遞迴str1就不等於空的字串值,就丟進去並且直接
          return str1  #return不下函數名稱str1 然後沒下函數名稱,之後返回就不會再丟入遞迴函數裡
      else :           # str1是空的就丟進這並且直接n轉str給str1之後直接return
          str1=str(n)+" "   #不下函數名稱直接返回 下方 並且不在丟入遞迴函數裡
          return str1
    else :             #如果n有值丟這
        str1=str(n%10)+" "+str1 #str1一次一次n%10取,取值轉str後再" "1格,之後加目前的str1之後丟給str1做生成值
        n=n//10           #每一次n%10取值完後,丟到這n//10取商,之後return在下函數名稱,把除完的n跟做生成值OK後
        return answer(n,str1) #的str1丟進去之後返回到下方,那這邊有下函數名稱,所以會在兩個值都遞迴回來
    
n=int(input())  #設1個n
str1=""      #跟空str1字串
print(answer(n,str1)) #丟入名稱answer(n,str1)並且去上方開始遞迴,遞迴到回來不能在遞迴為止


#EX: n->15 str1->""  遞迴前->n=15 str1="" 遞迴後 n=1 str1=str(n%10)+" "+str1 ->str1="5"+" "+str1 ->str1="5 "
# 遞迴前-> n=1 str1="5 " 遞迴後 n=0 str1(5 )=str(n%10)+" "+str1(5 ) ->str1(5 )="1 "+str1(5 ) -> str1="1 5 "
# 遞迴前n=0 str1="1 5 " 遞迴後 str1!="" return str1("1 5 ") 結束!

# n=0    n=15          n=128987871
#A:0      A:1 5         A:1 2 8 9 8 7 8 7 1 
