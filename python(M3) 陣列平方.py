arr=[]  #輸入arr為一維陣列
for i in range(0,4,1) : #0<4循環,每循環for 1次 arr+1次自己輸入的正整數 之後丟給自己(arr)
    arr+=[int(input())]
n=len(arr)             #算出arr一維陣列總長度
for j in range(0,n,1) : #用for j把長度丟進去,arr[j]目前位於j的值(平方)**2 乘完之後丟給sum
   sum=arr[j]**2            #sum生成值取平方完的值
   print(sum,end="\t")    #之後列印完再"\t",有下end所以這行不會自動換行
print()  #for j OK之後 print()直接列印 

#輸入:1  A:1   9   25  49 
#     3
#     5
#     7 