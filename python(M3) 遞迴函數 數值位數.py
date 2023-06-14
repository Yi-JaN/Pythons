#遞迴函數:數值位數     #python遞迴建議從遞迴結尾下方由下往上看比較看得懂
def f (x,count) :  #往上遞迴後,函數名稱對函數名稱,之後把x,count丟進遞迴函數
    if x>=1 :     #如果x>=1就丟進去
        count+=1  #count+1
        x=x//10   #丟進去的x除法取商數
        return f (x,count)  #然後這邊return有下函數名稱 所以丟回去下方會在丟回來
    else :       #這邊是如果我的x不是>=1 丟這
        return count  #直接return count ,那因為return這count沒下函數名稱,所以count丟回去下方,就可以不用
                      #丟回來上方做遞迴函數,然後x值卡死在else沒跟著一起return,所以就返回只有count
x=int(input())   #比方說我輸入4395
count=0         #count初始為0
print("計數為: ",f(x,count)) #下函數名稱"f"把x跟count丟進去,之後往上遞迴


#python遞迴跟JAVA遞迴很像,差就是差在JAVA由上至下看遞迴,python要由下再往上看遞迴循環

# x->4395     x->0        x->128917170
#計數為: 4    計數為: 0    計數為: 9
#   