#遞迴函數練習
#python這題遞迴函數跟Java不太一樣,python遞迴要先從遞迴函數下方由下至上到def函數裡面循環
def f(n) : #函數名稱對函數名稱就可丟進去 (如果回傳上來的分解值沒函數名稱則不得丟入此遞迴函數裡)
    if n==0 :
        return n+1 #而如果一開始的正整數或其中分解值是0,則+1,並且這裡沒下函數名稱,所以+1完該值丟回去不得在做遞迴
    elif n==1 :
        return n+1 #而如果一開始的正整數或其中分解值是1,則+1,並且這裡沒下函數名稱,所以+1完該值丟回去不得在做遞迴
    else :
        return f(n-1)+f(n//2) #此return有下函數名稱,所以分解完的值可丟回下方,在全部丟回上方做遞迴函數

n=int(input()) #輸入一個正整數
print(f(n)) #把我輸入的正整數丟到函數名稱為f裡面,之後往上丟進遞迴函數,函數名稱對函
            #數名稱

#補充:分解值意思是->意思是該正整數經過公式拆解形成的分解值,例如7丟入else裡分解為(6+3)
#                  ,分解值為6跟3!
#此題的遞迴函式題目
#
#f(n)=-> n+1 ,          when n=0,n=1
#     -> f(n-1)+f(n/2), when n>1
#

#題目輸入數學分解->7=(6+3)
#                  =(5+3)+(2+1)
#                  =(4+2)+(2+1)+(1+1)+(1) 
#                  =(3+2)+(1+1)+(1+1)+(1)+(1)+(1)+(1) 
#                  =(2+1)+(1+1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)
#                  =(1+1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)
#                  =(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)+(1)
#                  =分解完共有13個1,如果按照上述公式程式碼,13個1都n+1="26" <-

#輸入->7    輸入->10   輸入->12
#   A:26       A:60       A:94
#         
            