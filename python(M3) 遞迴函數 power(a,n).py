#此題有方法一及方法二  這題用方法一來寫
#方法一:power(a,n)=a*power(a,n-1)
#方法二:power(a,n)=a*power(a,n/2)*power(a,n/2) 當n為偶數
#      power(a,n)=a*power(a,n-1)              當n為奇數
def power(a,n) :  #由下至上函數名稱對函數名稱丟進去
    if n==1 :   #n==1,代表平方為1,平方為1就怎麼乘都是*1
        return a #所以直接取a值回去列印
    else : #其他只要平方大於1就進來
        return a*power(a,n-1) #以3 5來說,a(3)*power(a(3),n(5)-1);->丟回去的值變成a(3)*power(a(9),n(4));
                             #然後再丟a(3)*power(a(9),n(4)-1),以此類推,算到不能再算為止
    
a=int(input()) #以輸入3 5來說! a輸入3
n=int(input()) #n=輸入5  n做為平方
print(power(a,n)) #分別把a,n的值丟給函數名稱"power",然後由下至上丟入def函數

#題目:遞迴方法 power(a,n)
#題目詳請請去看模三題庫!
#          丟進來的值                丟回去的值
#3 5=a(3)*power(a(3),n(5)-1) ->power(a(9),n(4))
#   =a(3)*power(a(9),n(4)-1) ->power(a(27),n(3))
#   =a(3)*power(a(27),n(3)-1) ->power(a(81),n(2))
#   =a(3)*power(a(81),n(2)-1) ->power(a(243),n(1))
#  之後丟入if n==1 return a; 所以回去就只有a值,也就是243 之後就列印"243"這個值!
#  那為什麼前方的a(3)一直是a(3)呢? 因為a*a是乘給power,讓power裡的值做遞迴,所以你的a就只取第一次丟進來遞迴的那個a值
#輸入:(1.)2 3     A:(2.)3 5    A:(3.)2 10
#    A:8           A:243        A:1024        