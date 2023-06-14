#遞迴函數 最大公因數(非輾轉相除法)
def gcd(x,y) :
    maxx=max(x,y) #先取誰大誰小,分別給maxx跟minn
    minn=min(x,y)
    if maxx%minn!=0 :
        return gcd(minn,maxx%minn)
    else :
        return minn

n=int(input()) #輸入兩個值
m=int(input())
print(gcd(n,m)) #丟入gcd裡,函數名稱對函數名稱,然後n對x m對y,由下至上丟入def遞迴函數

#if maxx%minn!=0 -> 意思是這兩個值誰大誰小丟完後,判斷maxx%minn如果不等於0,就進入
#                   進入後用gcd函數名稱,gcd裡的x放目前的minn,y放maxx%minn的值都傳回去
#                   傳回去後,傳回去的值因為有下gcd函數名稱,所以可以名稱對名稱在由下至上
#                   丟進def遞迴函數,重頭到尾在run一次
#else            -> 這行意思是遞迴函數比到最後,最後的maxx跟minn%是0,就往下來到else裡,
#                   代表已經不在需要丟回去然後再由下至上傳上來做遞迴,並且也找到他們這兩個
#                   值彼此之間的"最大公因數",之後return minn,也就是回傳我目前的minn值回去
#                   下方的print括號裡,其他的值都沒傳回去,然後minn值傳回去之後也沒下gcd函數
#                   名稱,所以不能名稱對名稱再丟上來做遞迴,所以丟回去的minn值直接在print()裡
#                   列印就是答案!

#輸入->8 12      20 10
#輸出->4         10 