import random
score=[] #score陣列是一開始先取電腦的四位數的值,分別放在該陣列裡
arr=[] #arr是待會電腦四位數的值一個一個轉str放在arr陣列裡,這個是電腦裝的
for oo in range(0,1,1) : #for oo 取最高位數,最高位數第一個值不能為0,像9xxx就過關
    score+=[random.randint(1,9)]  #取1-9亂數產生給score+起來放在值0位置值 
for o in range(1,4,1) : #for o從1開始,1代表接下來從值1開始取,取接下來三個位數,然後要不重複
    score+=[random.randint(0,9)] #每循環1次取0-9亂數產生給score+起來放進去
    for x in range(0,o,1) : #每放進去1個就sop檢查剛剛放進去的值的前面的值有沒有重複
        if score[x]==score[o] : #有重複就進去,沒有就略過此if迴圈
            score[o]=random.randint(0,9) #針對剛剛位置值再重換一個0-9亂數產生
            if score[x]==score[o] : #如果換完那在檢查1次,如果又一樣在換,如果再檢查沒有就略過此if迴圈
                score[o]=random.randint(0,9)  #在1次針對剛剛位置值再重換一個0-9亂數產生               
for y in range(0,4,1) : #for y負責把score位置值裡的值一個一個轉str丟給arr一維陣列
    arr+=[str(score[y])]  #每循環1次取score目前的y位置值轉str後給arr陣列+起來
count=0 #count為我總共猜了幾次才猜中
a=0 #a為幾A幾B的A
b=0 #b為幾A幾B的B
z=True #這裡設布林數的True給z,此z是待會要丟while迴圈循環
while z : #當z為布林數的False,就停止該while迴圈循環
    data=[] #每循環一次這裡面的data一維陣列就歸空為空的一維陣列,data一維陣列是屬於你的!
    users=str(input("請輸入你所輸入的值: ")) #users為你猜的四位數的值,然後轉字串,每循環1次就猜一次
    count+=1 #猜一次值就count+1次
    for i in range(0,4,1) : #for i負責取你users猜的四位數的值,然後丟給data一維陣列
        data+=[users[i]] #每循環1次就取users目前i位置值的單字串給data一維陣列去+
    for j in range(0,4,1) : #for j是負責看我目前這輸入的值是幾A幾B
        if j==0 : #j是0就進去,進去就代表我自己data陣列中單獨取值0的位置值去審查
            if data[j]==arr[j] : #如果data值0跟arr電腦的陣列值0位置值是一樣的值就進去
                a+=1 #a就+1,代表找到一個值了,位置也相同
            elif data[j]==arr[1] or data[j]==arr[2] or data[j]==arr[3] : #但是如果是來到這邊就看data值0跟arr電腦陣列其他位置值有沒有一樣
                b+=1 #有就b+1,代表有找到,但是位置不同
        elif j==1 : #j是1就進去,意思跟上方的if j==0 :意思一模一樣,只不過就換成單獨取值1的位置值去審查
            if data[j]==arr[j] :
                a+=1
            elif data[j]==arr[0] or data[j]==arr[2] or data[j]==arr[3] :
                b+=1
        elif j==2 : #j是2就進去,意思跟上方if j==0 :意思一模一樣,只不過就換成單獨取值2的位置值去審查
            if data[j]==arr[j] :
                a+=1
            elif data[j]==arr[0] or data[j]==arr[1] or data[j]==arr[3] :
                b+=1
        elif j==3 : #j是3就進去,意思跟上方if j==0 :意思一模一樣,只不過就換成單獨取值3的位置值去審查
            if data[j]==arr[j] :
                a+=1
            elif data[j]==arr[0] or data[j]==arr[1] or data[j]==arr[2] :
                b+=1
    print(a,"A",b,"B") #for j ok之後,就看這組數字是找到幾A幾B
    if a==4 : #如果a==4就代表全部找到了,全部位置也相同
       print("電腦答案: ",arr) #就可以亮電腦的答案出來
       print("你的答案: ",data) #然後還有我的答案,做比對
       z=False #找到的話z就可以變False,可以停止此while迴圈循環
    a=0 #不管是不是找到,只要來到這裡a跟b歸0,假設沒全部找到,那就要歸0
    b=0 #給下次輸入的值去做尋找,不然不歸0,a跟b會一直累加,這樣是錯的
print("總共試了",count,"次")    #while z停止循環後往下來到這邊,看你猜了幾次才中
#python 幾A幾B
#規則:選定一組不重複的四位數數字,最高位數只能1-9,其他剩下三個位數能0-9
#注意:雖然是不重複但也有可能會出現重複數字,測試1次是50組出現1組              
#範例如下:
#請輸入你所輸入的值: 7653
#0 A 2 B
#請輸入你所輸入的值: 6172
#1 A 0 B
#請輸入你所輸入的值: 1672
#1 A 0 B
#請輸入你所輸入的值: 9074
#0 A 1 B
#請輸入你所輸入的值: 8702
#1 A 0 B
#請輸入你所輸入的值: 5932
#2 A 1 B
#請輸入你所輸入的值: 5872
#2 A 0 B
#請輸入你所輸入的值: 5302
#3 A 0 B
#請輸入你所輸入的值: 5312
#3 A 0 B
#請輸入你所輸入的值: 5362
#3 A 0 B
#請輸入你所輸入的值: 5342
#4 A 0 B
#電腦答案:  ['5', '3', '4', '2']
#你的答案:  ['5', '3', '4', '2']
#總共試了 11 次                