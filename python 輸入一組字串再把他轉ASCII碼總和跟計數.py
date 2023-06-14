#輸入一個字串並且算這字串的ASCII碼與字串出現的碼數
str1=str(input()) #輸入一組字串
n=len(str1)     #用len去算我的str1字串有幾個,待會要丟for迴圈循環拆開用,類似於java裡的str.length
sum=0           #sum總和ASCII碼
count=0         #count算這組字串有幾個字串
for i in range(0,n,1) : #這邊把len的n丟進去循環,str第一個單字串從0開始 0<8 1次++ +1
    count+=1            #循環1次count+1次
    m=ord(str1[i])     #這邊用m去拿我str1單字串,依照目前i值去拿單字串,拿到單字串轉ord
    sum=sum+m          #總和+我的m值
print("計數為: ",count)    
print("ASCII碼總合為: ",sum)    


# str1-> Abc123           ord就是轉"單"字串的ASCII碼  chr就是轉"單"ASCII碼的字串
# 計數為: 6
# ASCII碼總合為: 412