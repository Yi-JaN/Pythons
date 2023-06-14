import random
data=[] #先在此設一個陣列,data設為空陣列,此data陣列是待會要裝你輸入的驗證碼1個1個丟到這裡面
arr=[] #輸入一個空的陣列,此arr陣列為系統給的驗證碼
count=0 #count是用來看待會你輸入的碼跟他的驗證碼一個一個對,看有幾個一樣
for i in range(0,5,1) : #for i循環5次,意思是要設5個碼的驗證碼,每循環1次取1個碼到陣列
    arr+=[str(random.randint(0,9))] #arr陣列每循環就+亂數0-9出來的正整數轉字串的值
#print(arr)    
z=True #用布林式的True(是)先給z,待會要用z丟入外圈while迴圈循環
z1=True #用布林式的True(是)先給z1,待會要用z1丟入內圈while迴圈循環
while z : #while 是看z循環,z是布林式,只要布林式是True(是)就會一直循環,循環到變False(否)才會停止while循環
   for x in range(0,5,1) : #每循環1次來到這第一步先用for x一個一個列印arr陣列上的字串值(驗證碼)出來
       if x==0 : #如果x是0就進去
           print(arr[x],end="") #列印arr陣列裡值0的驗證碼,並且在+""(空字串)
       elif x==1 : #如果x是1就進去
           print(arr[x],end="") #列印arr陣列裡值1的驗證碼,並且在+""(空字串)
       elif x==2 : #如果x是2就進去
           print(arr[x],end="") #列印arr陣列裡值2的驗證碼,並且在+""(空字串)
       elif x==3 : #如果x是3就進去
           print(arr[x],end="") #列印arr陣列裡值3的驗證碼,並且在+""(空字串)
       elif x==4 : #如果x是4就進去
           print(arr[x],end="") #列印arr陣列裡值4的驗證碼,並且在+""(空字串)
   print() #等到for x循環後在下print()代表換行
   count1=0 #這裡設一個count1=0,count1是待會要看你str1有幾個單字串組合成一組字串
   while z1 : #while 是看z1循環,z1是布林式,只要布林式是True(是)就會一直循環,循環到變False(否)才會停止內圈while循環
      data=[] #每循環1次確保都先歸為空字串,因為待會要用他取你str1的單字串丟入此陣列裡
      str1=str(input("請輸入驗證碼: ")) #str1代表你輸入的驗證碼
      count1=len(str1) #count1是看你str1的長度
      if count1==5 : #如果count1長度是5就進去,不是的話就略過,然後就一直跑內圈while,跑到是count1==5為止
          z1=False #進去後z1可以歸False,代表我輸入的驗證碼代表長度為5
   for j in range(0,5,1) : #for j循環5次,每循環1次就1個驗證碼丟進data陣列
       data+=[str1[j]] #每循環1次就+str1的j位置值的單字串(驗證碼)給data陣列
   #print(data)
   for k in range(0,5,1) : #for k就是看你輸入的驗證碼跟他的驗證碼是否符合
       if k==0 : #如果k是0就進去
           if data[k]==arr[k] : #雙方取我符合外圈if的k值做比較,一樣則進去
               count+=1 #count就+1
       elif k==1 : #如果k是1就進去
           if data[k]==arr[k] : #雙方取我符合外圈elif的k值做比較,一樣則進去
               count+=1 #count就+1
       elif k==2 : #如果k是2就進去
           if data[k]==arr[k] : #雙方取我符合外圈elif的k值做比較,一樣則進去
               count+=1 #count就+1
       elif k==3 : #如果k是3就進去
           if data[k]==arr[k] : #雙方取我符合外圈elif的k值做比較,一樣則進去
               count+=1 #count就+1
       elif k==4 : #如果k是4就進去
           if data[k]==arr[k] : #雙方取我符合外圈elif的k值做比較,一樣則進去
               count+=1 #count就+1   
   if count==5 : #如果來到這邊就是代表我看此count是不是5,是->符合就進去
       print("驗證完成!") #顯示"驗證完成"
       z=False        #z變為False(否),因為成功符合,所以該外圈while不用再循環了
   else : #來到此else代表可能是其他因素,像是驗證碼輸入錯誤...等
      print("輸入錯誤!") #一樣顯示"輸入錯誤!"
      arr=[] #arr陣列來到這邊設空陣列,意思是待會要重新換一組驗證碼
      for i2 in range(0,5,1) :
          arr+=[str(random.randint(0,9))]
      count=0 #count歸0,待會要再輸入一次
      z1=True #z1在回歸為True(是),因為待會要再輸入一次所以內圈while z1要再循環取你輸入的驗證碼字串
#範例輸入如下
#    範例1                      範例2                         範例3
#20895                          72888                        95385
#請輸入驗證碼: 208               請輸入驗證碼: 72887          請輸入驗證碼: 95385
#請輸入驗證碼: 2089              輸入錯誤!                    驗證完成!
#請輸入驗證碼: 208955            57478
#請輸入驗證碼: 20895             請輸入驗證碼: 57478
#驗證完成!                       驗證完成!