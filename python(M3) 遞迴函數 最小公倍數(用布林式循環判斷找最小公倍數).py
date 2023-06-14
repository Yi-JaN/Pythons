def f(x,y) :
    z=True #一開始設一個z,然後給他布林式的True,這樣可以讓他一開始while可以進去循環並且判斷最小公倍數
    if x>y :
        dep=x
    elif x<y:
        dep=y
    while z :
        if dep%x==0 and dep%y==0 :
            gcd=dep
            z=False #找到符合此兩數的最小公倍數後在把z變成False,讓他接下來while不能再循環
        dep+=1
    return gcd     
            

n=int(input())
m=int(input())
print(f(n,m))

#while True ->True代表是"是",所以while會一直循環
#z=False ->z變成False 代表我while放z,這時候while z =->while False,所以while變
#          False已經不能循環while

#輸入->54 24    8 12
#輸出->216      24