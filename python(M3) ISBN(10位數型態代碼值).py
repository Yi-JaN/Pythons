str1=str(input()) #輸入一串ISBN碼
arr1=[] #arr1的陣列是要拿來取第一次累加和
arr2=[] #arr2的陣列是要拿來取第二次累加和
a=len(str1) #先算該字串長度,待會要先做str1的第一次累加和
summ1=0 #summ1是負責+str1每個單字串轉int值的累加和
summ2=0 #summ2是負責+arr1陣列裡面的第一次累加和然後進而產生出第二次累加和
allisbn=0 #allisbn是負責取最終第二次累加和的總和
for i in range(0,a,1) : #for i負責做第一次累加和
    ch=str1[i] #每循環1次取str1的i位置值的單字串給ch做生成值
    if ch=='X' and i==9 : #如果ch=='X' 和 位置值i是9(也就是取str1第10個單字串)就進去 
       summ1+=10 #summ1就+10,因為X代表此位數碼是10
       chstr=str(summ1) #累加的summ1轉str給裡面的chstr做生成值
       arr1+=[chstr] #然後推給arr1一維陣列
    elif ch>='0' and ch<='9' : #其他如果現在的ch是0~9就進去
        chint=int(ch) #進去轉int值給裡面的chint做生成值
        summ1+=chint  #summ1做生成值(生成+來自chint的值做生成),進行累加
        chstr=str(summ1) #累加的summ1轉str給chstr做生成值
        arr1+=[chstr] #然後推給arr1一維陣列
    else : #其他ch不是X and i位置值是9  或者ch不是位於0~9就進入
        break #然後下停頓,脫離整個if迴圈後再脫離整個for i
aa=len(arr1) #aa為arr1一維陣列的長度值,待會要用arr1的陣列算第二次累加值,然後也進階提前知道了ISBN是幾位數的編碼
for x in range(0,aa,1) : #for x負責做第二次累加值
    ch=arr1[x] #取arr1目前x位置值裡的單字串給ch做生成值
    chint2=int(ch) #然後生成值後的ch轉int值給for x裡面的chint2
    summ2+=chint2 #summ2做生成值(生成+來自chint2的值做生成),進行第二次累加
    arr2+=[int(summ2)]  #目前的summ2轉int值,然後推給arr2一維陣列   
arr2.sort(reverse=True) #for x ok後,arr2的陣列用遞增排序,由小至大,由小至大後再用reverse,做由大至小
allisbn=int(arr2[0]) #reverse OK之後取由大至小的arr[0],也就是最大值取給allisbn
print(allisbn) #然後列印該ISBN驗證碼
if allisbn%11==0 and aa==10 : #如果allisbn可以被11整除和 aa長度值確定是10位數型態邊碼就進去
    print("YES") #進去顯示"YES"
else : #if不是就近else(無條件進入)
    print("NO")    #進去顯示"NO" 

#ISBN是一種世界共通書籍邊碼,此編碼為10位數型態邊碼,所以此碼由十個位數組成,每一位數可以
#為0~9任何一個數字,或者為X,X代表此位數是10,如果此10碼的ISBN可以被11整除,也就是為11的倍
#數,則此通過ISBN驗證為合法碼

#ISBN碼        0    1   3   1   6    2    9    5    9    10(X)
#第一次累加和   0    1   4   5   11   13   22   27   36   46
#第二次累加和   0    1   5   10  21   34   56   83   119  165
#經由計算可得其識別碼為165 乃是11之倍數,故此為ISBN的合法驗證碼

#輸入說明:輸入一串ISBN碼

#補充:reverse->反向列表中的元素!

#輸入->013162959X   0131629599   013162959x     986133016X   
#輸出->165          164          119            275
#輸出->YES          NO           NO             YES