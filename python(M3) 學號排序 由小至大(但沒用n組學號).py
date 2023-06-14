#學號排序 由小到大(沒用n組學號版本)
n=input()  #輸入一組一維陣列
arr=[int(j) for j in n.split()] #丟入arr 讓j取n.split() 之後每取一個n的單字符串再丟入int(j)轉正整數再丟給arr
m=len(arr)   #算arr一維陣列長度
arr.sort()   #arr丟入sort 遞增排序,並且這是由小至大
for i in range(0,m,1) :  #用for把m長度丟進去,一個一個取值再丟給sum,在每列一個值下去
   sum=arr[i]           #列印時,順便由小至大排序
   print(sum)    
   
   

#補充: arr=[int(j) for j in n.split()] 詳請請翻筆記,(python 一維陣列)   

#103021020 105074011 102033058
#A:102033058
#  103021020
#  105074011