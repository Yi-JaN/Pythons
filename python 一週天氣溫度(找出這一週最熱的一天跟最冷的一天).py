data=[] #此一維陣列是拿來做取一週天氣溫度的動作
arr=["禮拜一","禮拜二","禮拜三","禮拜四","禮拜五","禮拜六","禮拜日"] #此arr一維陣列是一週7天
for a in range(0,7,1) : #取7個值(天氣溫度),陣列開頭第一個值為0,所以for a一開始為0
    data+=[int(input())] #每循環1次就取自己設的值轉int值推給data一維陣列
dataall=data[:] #設一個dataall,dataall是待會要列印禮拜一到禮拜日的天氣溫度
arrall=arr[:] #設一個arrall,arrall是待會要列印禮拜一到禮拜日的日子,搭配dataall一起看    
data1=data[:] #設一個data1,data1是待會找最冷的天氣溫度 
arr1=arr[:] #設一個arr1,arr1是待會找最冷的天氣溫度的日子   
a=len(data) #算data一維陣列長度值
for i in range(0,a,1) : #這裡for是做泡沫排序,for i為外圈,先做找最熱的天氣溫度
    for j in range(0,(a-1),1) : #for j為內圈,也是做泡沫排序主要地方
        if data[j]<data[j+1] : #如果目前的j比下一個j還要小就互換位置,而<是由大至小
            xxx=data[j]
            data[j]=data[j+1]
            data[j+1]=xxx
            yyy=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=yyy
hotmath=int(data[0]) #取出最熱的天氣溫度
hotday=str(arr[0])   #取出最熱的天氣溫度的日子
aa=len(data1)
for x in range(0,aa,1) : #這裡for是做泡沫排序,for x為外圈,再來做找最冷的天氣溫度
    for y in range(0,(aa-1),1) : #for y為內圈,也是做泡沫排序主要地方
        if data1[y]>data1[y+1] : #如果目前的y比下一個y還要大就互換位置,而>是由小至大
            xxxx=data1[y]
            data1[y]=data1[y+1]
            data1[y+1]=xxxx
            yyyy=arr1[y]
            arr1[y]=arr1[y+1]
            arr1[y+1]=yyyy
coldmath=int(data1[0]) #取出最冷的天氣溫度
coldday=str(arr1[0])   #取出最冷的天氣溫度的日子
print("一週天氣溫度->",dataall) #列印一週天氣溫度
print("一週日子   ->",arrall) #列印一週天氣溫度的日子,搭配dataall一起看
print("這一週最熱的一天是:"+hotday,"->",hotmath,"度") #剛剛泡沫排序後最熱的一天跟日子列印出來
print("這一週最冷的一天是:"+coldday,"->",coldmath,"度") #剛剛泡沫排序後最冷的一天跟日子列印出來         
           


#補充:泡沫排序->由兩個for迴圈架構而成,一個為外圈for 一個為內圈for,外圈for是看我天氣溫度(data)
#              有幾個值,他就循環外圈幾次,每一次循環盡量幫助內圈for達到最完美狀態的泡沫排序由
#              小至大,或由大至小,循環到外圈for結束,就是最完美狀態的泡沫排序
#              內圈for是在做泡沫排序由小至大,或由大至小的地方

#補充2:[:] ->[:]是負責取某一維陣列裡一模一樣的位置值裡的值出來給另一個一維陣列,像上方程式碼的
#            data1=data[:],意思就是取data一模一樣的值給data1,所以data1就有跟data一模一樣的
#            一維陣列

#一週天氣溫度->[16,38,31,12,17,7,22]
#一週日子   ->['禮拜一','禮拜二','禮拜三','禮拜四','禮拜五','禮拜六','禮拜日']
#這一週最熱的一天是:禮拜二->38度
#這一週最冷的一天是:禮拜六->7度