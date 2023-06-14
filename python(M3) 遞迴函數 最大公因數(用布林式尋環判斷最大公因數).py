def answer(x,y) :
   z=True #一開始設一個z,然後給他布林式的True,這樣可以讓他一開始while可以進去循環並且判斷最大公因數
   minn=min(x,y) #找此兩個值的最小值,並且待會while從最小值依序遞減找出彼此之間的最大公因數
   gcd=0 #此gcd是待會要拿你們彼此之間的最大公因數
   while z :
       if x%minn==0 and y%minn==0 :
           gcd=minn
           z=False #找到符合此兩數的最大公因數後在把z變成False,讓他接下來while不能再循環
       minn-=1
   return gcd
    
n=int(input())
m=int(input())
print(answer(n,m))#丟給名稱為answer裡,然後由下至上函數名稱對函數名稱丟入def遞迴函數 

#while True ->True代表是"是",所以while會一直循環
#z=False ->z變成False 代表我while放z,這時候while z =->while False,所以while變
#          False已經不能循環while   

#輸入->8 12  54 24
#輸出->4     6