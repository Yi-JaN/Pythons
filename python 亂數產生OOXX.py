import random
#亂數產生圈圈叉叉  圈為0 叉為1
data=[[]] #先輸入一個空白的二維陣列,名稱為data,然後待會data二維陣列會先用單字串代表預設
users=random.randint(0,1) #讓使用者一開始亂數當0或1 是0的話待會換位置值就是為數字單字串'0' 是1的話待會換位置值就是為數字單字串'1'
print(users) #列印我使用者的身份
arr=[] #輸入一個一維陣列
for o in range(0,3,1) : #只有3次隨機亂數機會,陣列開頭必為0 所以0<3 每循還1次+1
    arr+=[random.randint(1,9)]
    for oo in range(0,o,1) :
        if arr[o]==arr[oo] : #如果目前arr裡面的位置o跟我這位置o前面的值有重覆
            arr[o]=random.randint(1,9) #就針對我這位置o的值"再"亂數產生1個值
print(arr)  #來到這裡就是亂數產生3個值(不重覆)結束,先列印arr結果       
if users==0 : #使用者是0的話進入
    data=[['A','B','C'],['D','E','F'],['G','H','I']] #使用者是0,data一開始就預設為單字串                                  
    for i in range(0,3,1) : #把亂數產生3個值(不重覆)丟進這,做更改data二維陣列"位置"的動作
        if i==0 :
            if arr[i]==1 :   
                data[0][0]='0'
            elif arr[i]==2 :
                data[0][1]='0'
            elif arr[i]==3 :
                data[0][2]='0'
            elif arr[i]==4 :
                data[1][0]='0'
            elif arr[i]==5 :
                data[1][1]='0'
            elif arr[i]==6 :
                data[1][2]='0'
            elif arr[i]==7 :
                data[2][0]='0'
            elif arr[i]==8 :
                data[2][1]='0'
            elif arr[i]==9 :
                data[2][2]='0'
        elif i==1 :
            if arr[i]==1 :
                data[0][0]='0'
            elif arr[i]==2 :
                data[0][1]='0'
            elif arr[i]==3 :
                data[0][2]='0'
            elif arr[i]==4 :
                data[1][0]='0'
            elif arr[i]==5 :
                data[1][1]='0'
            elif arr[i]==6 :
                data[1][2]='0'
            elif arr[i]==7 :
                data[2][0]='0'
            elif arr[i]==8 :
                data[2][1]='0'
            elif arr[i]==9 :
                data[2][2]='0'
        elif i==2 :
            if arr[i]==1 :
                data[0][0]='0'
            elif arr[i]==2 :
                data[0][1]='0'
            elif arr[i]==3 :
                data[0][2]='0'
            elif arr[i]==4 :
                data[1][0]='0'
            elif arr[i]==5 :
                data[1][1]='0'
            elif arr[i]==6 :
                data[1][2]='0'
            elif arr[i]==7 :
                data[2][0]='0'
            elif arr[i]==8 :
                data[2][1]='0'
            elif arr[i]==9 :
                data[2][2]='0'
elif users==1 : #使用者是1的話就來到這進入
    data=[['A','B','C'],['D','E','F'],['G','H','I']] #使用者是1,那data二維陣列一開始預設為單字串
    for i1 in range(0,3,1) : #把亂數產生3個值(不重覆)丟進這,做更改data二維陣列"位置"的動作
        if i1==0 :
            if arr[i1]==1 :
                data[0][0]='1'
            elif arr[i1]==2 :
                data[0][1]='1'
            elif arr[i1]==3 :
                data[0][2]='1'
            elif arr[i1]==4 :
                data[1][0]='1'
            elif arr[i1]==5 :
                data[1][1]='1'
            elif arr[i1]==6 :
                data[1][2]='1'
            elif arr[i1]==7 :
                data[2][0]='1'
            elif arr[i1]==8 :
                data[2][1]='1'
            elif arr[i1]==9 :
                data[2][2]='1'
        elif i1==1 :
            if arr[i1]==1 :
                data[0][0]='1'
            elif arr[i1]==2 :
                data[0][1]='1'
            elif arr[i1]==3 :
                data[0][2]='1'
            elif arr[i1]==4 :
                data[1][0]='1'
            elif arr[i1]==5 :
                data[1][1]='1'
            elif arr[i1]==6 :
                data[1][2]='1'
            elif arr[i1]==7 :
                data[2][0]='1'
            elif arr[i1]==8 :
                data[2][1]='1'
            elif arr[i1]==9 :
                data[2][2]='1'
        elif i1==2 :
            if arr[i1]==1 :
                data[0][0]='1'
            elif arr[i1]==2 :
                data[0][1]='1'
            elif arr[i1]==3 :
                data[0][2]='1'
            elif arr[i1]==4 :
                data[1][0]='1'
            elif arr[i1]==5 :
                data[1][1]='1'
            elif arr[i1]==6 :
                data[1][2]='1'
            elif arr[i1]==7 :
                data[2][0]='1'
            elif arr[i1]==8 :
                data[2][1]='1'
            elif arr[i1]==9 :
                data[2][2]='1'
for j in range(0,3,1) : #這裡就是列印data二維陣列,來到這邊代表已經OOXX結束,"要列印結果出來"
    for k in range(0,3,1) :
        print(data[j][k],end=" ")
    print()
if data[0][0]==data[0][1] and data[0][1]==data[0][2] and data[0][2]==data[0][0] : #中第一條
    print("in one")    
elif data[1][0]==data[1][1] and data[1][1]==data[1][2] and data[1][2]==data[1][0] : #中第二條
    print("in two")
elif data[2][0]==data[2][1] and data[2][1]==data[2][2] and data[2][2]==data[2][0] : #中第三條
    print("in three")
elif data[0][0]==data[1][0] and data[1][0]==data[2][0] and data[2][0]==data[0][0] : #中第四條
    print("in four")
elif data[0][1]==data[1][1] and data[1][1]==data[2][1] and data[2][1]==data[0][1] : #中第五條
    print("in five")
elif data[0][2]==data[1][2] and data[1][2]==data[2][2] and data[2][2]==data[0][2] : #中第六條
    print("in six")
elif data[0][2]==data[1][1] and data[1][1]==data[2][0] and data[2][0]==data[0][2] : #中第七條
    print("in seven")
elif data[0][0]==data[1][1] and data[1][1]==data[2][2] and data[2][2]==data[0][0] : #中第八條
    print("in eight")
else :  #上面1到8條沒中任何一個就來到這邊,代表沒中任何一條
    print("No a every")    
#說明圖如下:
#範例: 1 2 3 <-左邊為OOXX的九宮格,而數字代表他的位置,例如6就是高1值2的位置,所以針對
#      4 5 6   高1值2的位置做你users拿到的數字做更改,所以users拿到的數字是1,那就是
#      7 8 9   高1值2的位置更改成單字串的'1'
#說明(2)如下:
#data的二維陣列中,data[0][0] data[0][1] data[0][2]為中one, data[1][0] data[1][1] data[1][2]為中two,
#data[2][0] data[2][1] data[2][2]為中three, data[0][0] data[1][0] data[2][0]為中four, data[0][1]
#data[1][1] data[2][1]為中five, data[0][2] data[1][2] data[2][2]為中six, data[0][2] data[1][1]
#data[2][0]為中seven, data[0][0] data[1][1] data[2][2]為中eight

#程式循環步驟-> 步驟一:先亂數取得users的數字  步驟二:取隨機3個亂數(不重覆)到一維陣列
#              步驟三:根據users的數字對應符合的if迴圈 步驟四:更改data二維陣列的位置值,依據我亂數拿到的值,然後針對拿到的值做位置值的修改
#              步驟五:顯示修改後的data二維陣列,列印九宮格出來   步驟六:最下面if迴圈判斷中哪一條,或者不中任何一條

#隨機產生答案如下:
#0            1               0              1
#[4,9,7]      [4,8,2]         [7,1,4]        [4,5,6]   
#A B C        A 1 C           0 B C          A B C
#0 E F        1 E F           0 E F          1 1 1
#0 H 0        G 1 I           0 H I          G H I
#No a every   No a every      in four        in two
