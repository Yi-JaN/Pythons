#輸入1個n值,並且n到1之間有幾個質數 (遞迴函數)
#遞迴函數在python看法是先由下再往上進入def函式循環
def answer(x,count) : #由下至上後函數名稱對函數名稱,把值丟進來 x<->n count<->count
    if x>=1 : #看你目前的x(n)是不是大於等於1(>=1)
        p=1   #每次丟入if迴圈進來後p都要=1
        count1=0 #然後計數歸0 (此計數是算目前這個x(n)值有幾個因數,進而判斷是不是質數)
        while p<=x : #然後用while做"質數判斷"
            if x%p==0 : #如果目前的x(n)值%p餘數是0,代表此p值是目前x(n)的因數
                count1+=1 #符合進入後count1 +1
            p+=1   #此p值循環到這邊不管是不是目前x(n)的因數都要在+1,做下一個p值的循環判斷
        if count1==2 : #while質數判斷完畢後丟入這邊,如果count1是2代表目前的x(n)是質數
            count+=1  #然後count +1,代表找到1個值是質數
            x=x-1    #找到後目前x(n)去-1
            return answer(x,count) #然後把目前的x(n)跟count return回去,注意:這邊有下函數名稱answer,所以丟回去下方會再丟回來上方做遞迴函數
        else :  #如果count1不是2的話就丟來這邊,然後代表我目前的x(n)不是質數
            x=x-1 #然後不是質數就把目前x(n) -1
            return answer(x,count) #然後把目前的x(n)跟count return回去,注意:這邊有下函數名稱answer,所以丟回去下方會再丟回來上方做遞迴函數
    else :  #如果目前的x(n)一開始if x>=1 判斷不是>=1 就丟來這
        return count #然後就把目前的count return回去,注意:這邊return沒有下函數名稱,所以return count後,該值丟回去就"不能"丟回來上方做遞迴函數

n=int(input()) #輸入一個正整數
count=0 #此用來算有幾個質數
print(answer(n,count)) #之後把正整數跟計算幾個質數丟入名為answer函數名稱裡,然後再去
                       #上方丟入def函式

#輸入n->100   輸入n->80
#  A:25         A:22               