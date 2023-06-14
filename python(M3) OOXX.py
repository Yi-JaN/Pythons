#圈圈叉叉 0為圈 1為叉
data=[[0]*3 for o in range(3)] #圈圈叉叉我們可以用二維陣列去設,這樣待會列印時會呈現9宮格出來,用一個3x3矩陣(高給3個值給3個)
for x in range(0,3,1) : #for i為高,這裡取0跟1給他
    for y in range(0,3,1) : #for j為值
        data[x][y]=int(input()) #每循環1次取1個我輸入的值轉int後丟給目前data二維陣列上的高x值y位置上       
for i in range(0,3,1) : #for i為高,這裡就是慢慢列印用二維陣列列印出來的9宮格
    for j in range(0,3,1) : #for j為值
        print(data[i][j],end=" ")#每循環1次取data目前的i高j值位置上的值,然後再空格
    print()  #列印完一行後換行,換再下一行列印
if data[0][0]==data[0][1] and data[0][1]==data[0][2] and data[0][2]==data[0][0] : #如果是高0值0到高0值2是一樣,代表一條線連線,那就進去
    print("True")    #顯示為True
elif data[1][0]==data[1][1] and data[1][1]==data[1][2] and data[1][2]==data[1][0] : #如果是高1值0到高1值2是一樣,代表一條線連線,那就進去
    print("True")
elif data[2][0]==data[2][1] and data[2][1]==data[2][2] and data[2][2]==data[2][0] : #如果是高2值0到高2值2是一樣,代表一條線連線,那就進去
    print("True")
elif data[0][0]==data[1][0] and data[1][0]==data[2][0] and data[2][0]==data[0][0] : #如果是高0值0 高1值0 高2值0一樣,代表一條線連線,那就進去
    print("True")
elif data[0][1]==data[1][1] and data[1][1]==data[2][1] and data[2][1]==data[0][1] : #如果是高0值1 高1值1 高2值1一樣,代表一條線連線,那就進去
    print("True")
elif data[0][2]==data[1][2] and data[1][2]==data[2][2] and data[2][2]==data[0][2] : #如果是高0值2 高1值2 高2值2一樣,代表一條線連線,那就進去
    print("True")
elif data[0][0]==data[1][1] and data[1][1]==data[2][2] and data[2][2]==data[0][0] : #如果是高0值0 高1值1 高2值2一樣,代表一條線連線,那就進去
    print("True")
elif data[0][2]==data[1][1] and data[1][1]==data[2][0] and data[2][0]==data[0][2] : #如果是高0值2 高1值1 高2值0一樣,代表一條線連線,那就進去
    print("True")
else : #只要不符合上述8種連線方式,就來else裡
    print("False")     #顯示為False
    
#輸入->0 0 1            1 0 0         1 0 0
#      1 0 0            0 1 1         0 1 0
#      1 0 1            1 1 0         1 0 1
#輸出->True             False         True