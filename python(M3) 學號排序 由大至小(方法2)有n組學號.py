#學號排序 由大至小
m=int(input())  #輸入一組資料型態正整數
arr=[]          #輸入arr為一維陣列
for i in range(0,m,1) : #把資料型態正整數丟到for裡,for每循環1次 arr+1次自己取的正整數 之後丟給自己(arr)
    arr+=[int(input())]
n=len(arr)           #for i OK之後 最後arr一維陣列先拿來算長度
arr.sort(reverse=True)  #把arr丟入sort遞增排序,並且reverse意思是"反向"列表中元素 True為是
for j in range(0,n,1) : #把長度丟入for j 並且每循環一次,arr[j](目前位於j值)
    sum=arr[j]           #就丟給sum給他去做生成值
    print(sum)     #sum生成值的值列印,列印完同時在由大至小排序!


#reverse=True 意思是"反向"列表中的元素  True為是   

#3              A:
#103021020       105074011
#105074011       103021020
#102033058       102033058