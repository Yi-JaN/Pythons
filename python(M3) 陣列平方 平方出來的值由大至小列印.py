#陣列平方  平方出來的值由大至小列印
arr=[]   #輸入arr為一維陣列
for i in range(0,4,1) :  #0<4 for每循環一次  arr+1次自己取的正整數 之後丟給自己
    arr+=[int(input())]
n=len(arr)             #把最後arr一維陣列的長度用len算出來
arr.sort(reverse=True)  #把arr陣列丟入sort遞增排序 由大至小
for j in range(0,n,1) :  #把算出來的長度丟入for j  每循環一次 arr[j](目前位於的j值)
   sum=arr[j]**2         #就先平方**2 之後丟給sum生成值
   print(sum,end="\t")  #之後sum生成值的值丟入這列印,然後再"\t",那因為有下end 所以不會換行字元
print()  #最後for j循環OK之後,print()換行字元

#reverse=True 意思是取"反向"列表中的元素 True為是

#輸入:1   A:49  25  9   1   輸入:2   A:81  16  9   4
#     3                         4
#     5                         3
#     7                         9