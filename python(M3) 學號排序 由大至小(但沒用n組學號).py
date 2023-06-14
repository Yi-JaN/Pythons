#學號排序 由大至小 (但沒輸入n組學號)
n=input()   #輸入一組一維陣列
arr=[int(i) for i in n.split()] #把n丟入arr 並用n.split 用for原理去取n值 i就去取n的單字符串 每取到1個字符串再丟int(i) 之後給arr
a=len(arr)    #a去取我arr一維陣列的長度
arr.sort(reverse=True) #arr用sort遞增排序,這邊用reverse=True 代表arr全部值由大至小排序
for j in range(0,a,1) : #用for迴圈一個一個取arr的陣列值,把長度放進去 陣列開頭為0
    sum=arr[j]     #每取一個arr[j]位於的j值丟給sum做sum的生成值
    print(sum)   #之後列印拿到的sum 列印完並且在由大至小排序
    
#arr=[int(i) for i in n.split()] 詳請請去筆記 (python 一維陣列)去看   
#reverse=True 意思是"反向"列表中的元素,所以arr才會由大至小排序,True為是