data=[["1","0","4","0","0","0"],
      ["4","0","4","0","4","0"],
      ["4","0","4","0","4","0"],
      ["4","0","4","0","4","0"],
      ["4","0","0","0","4","0"]] #data設定為一個二維陣列,也就是迷宮圖高5(高4+高0)值6(值5+值0)的二維陣列
for i in range(0,5,1) : #for i跟for x是先列印目前data二維陣列的模樣
    for x in range(0,6,1) :
        print(data[i][x],end="\t")
    print()    
z=True #z設定為一個布林代數的True
while z : #z放入條件式,每次循環如果z是True代表是(要),就繼續循環,如果是False代表否(不要),就停止該while迴圈循環
    n=int(input("選擇你要走的方向(1/2/3/4): ")) #n設定為取你輸入的值轉int,也是應用於迷宮圖的走路方向
    if n==1 : #如果n為1代表往左,是1就進入
        if data[0][1]=="1" : #看目前"1"的位置,此條件式是找可以往左循環的高幾值幾陣列(1個1個找)
            data[0][1]="0" #目前位置先歸"0"
            data[0][0]="1" #然後往左就是高0值0可行走之地方,在設置為"1"
            for i01 in range(0,5,1) : #設置完用for i01跟j01去列印顯示目前模樣
                for j01 in range(0,6,1) :
                    print(data[i01][j01],end="\t")
                print()
        elif data[4][2]=="1" : #同步if data[0][1]=="1"意思
            data[4][2]="0"
            data[4][1]="1"
            for i02 in range(0,5,1) :
                for j02 in range(0,6,1) :
                    print(data[i02][j02],end="\t")
                print()
        elif data[4][3]=="1" : #同步if data[0][1]=="1"意思
            data[4][3]="0"
            data[4][2]="1"
            for i03 in range(0,5,1) :
                for j03 in range(0,6,1) :
                    print(data[i03][j03],end="\t")
                print()
        elif data[0][4]=="1" : #同步if data[0][1]=="1"意思
            data[0][4]="0"
            data[0][3]="1"
            for i04 in range(0,5,1) :
                for j04 in range(0,6,1) :
                    print(data[i04][j04],end="\t")
                print()
        elif data[0][5]=="1" : #同步if data[0][1]=="1"意思
            data[0][5]="0"
            data[0][4]="1"
            for i05 in range(0,5,1) :
                for j05 in range(0,6,1) :
                    print(data[i05][j05],end="\t")
                print()
        else : #來到這裡代表,上述可以往左的都找過了但是都沒有找到"1",所以來到這進入
            print("往左走就碰壁了!")
            for i06 in range(0,5,1) :
                for j07 in range(0,6,1) :
                    print(data[i06][j07],end="\t")
                print()
    elif n==2 : #如果n為2代表往右,是2就進入
        if data[0][0]=="1" : #看目前"1"的位置,此條件式是找可以往右循環的高幾值幾陣列(1個1個找)
            data[0][0]="0" #目前位置先歸"0"
            data[0][1]="1" #然後往右就是高0值1可行走之地方,在設置為"1"
            for q01 in range(0,5,1) : #設置完用for q01跟w01去列印顯示目前模樣
                for w01 in range(0,6,1) :
                    print(data[q01][w01],end="\t")
                print()    
        elif data[4][1]=="1" : ##同步if data[0][0]=="1"意思
            data[4][1]="0"
            data[4][2]="1"
            for q02 in range(0,5,1) :
                for w02 in range(0,6,1) :
                    print(data[q02][w02],end="\t")
                print()
        elif data[4][2]=="1" : #同步if data[0][0]=="1"意思
            data[4][2]="0"
            data[4][3]="1"
            for q03 in range(0,5,1) :
                for w03 in range(0,6,1) :
                    print(data[q03][w03],end="\t")
                print()
        elif data[0][3]=="1" : #同步if data[0][0]=="1"意思
            data[0][3]="0"
            data[0][4]="1"
            for q04 in range(0,5,1) :
                for w04 in range(0,6,1) :
                    print(data[q04][w04],end="\t")
                print()
        elif data[0][4]=="1" : #同步if data[0][0]=="1"意思
            data[0][4]="0"
            data[0][5]="1"
            for q05 in range(0,5,1) :
                for w05 in range(0,6,1) :
                    print(data[q05][w05],end="\t")
                print()
        else : #來到這裡代表,上述可以往右的都找過了但是都沒有找到"1",所以來到這進入
            print("往右走就碰壁了!")
            for q06 in range(0,5,1) :
                for w06 in range(0,6,1) :
                    print(data[q06][w06],end="\t")
                print()
    elif n==3 : #如果n為3代表往上,是3就進入
        if data[1][1]=="1" : #看目前"1"的位置,此條件式是找可以往上循環的高幾值幾陣列(1個1個找)
            data[1][1]="0"  #目前位置先歸"0"
            data[0][1]="1"  #然後往上就是高0值1可行走之地方,在設置為"1"
            for a01 in range(0,5,1) : #設置完用for a01跟b01去列印顯示目前模樣
                for b01 in range(0,6,1) :
                    print(data[a01][b01],end="\t")
                print()
        elif data[2][1]=="1" : #同步於if data[1][1]=="1"意思
            data[2][1]="0"
            data[1][1]="1"
            for a02 in range(0,5,1) :
                for b02 in range(0,6,1) :
                    print(data[a02][b02],end="\t")
                print()
        elif data[3][1]=="1" : #同步於if data[1][1]=="1"意思
            data[3][1]="0"
            data[2][1]="1"
            for a03 in range(0,5,1) :
                for b03 in range(0,6,1) :
                    print(data[a03][b03],end="\t")
                print()
        elif data[4][1]=="1" : #同步於if data[1][1]=="1"意思
            data[4][1]="0"
            data[3][1]="1"
            for a04 in range(0,5,1) :
                for b04 in range(0,6,1) :
                    print(data[a04][b04],end="\t")
                print()
        elif data[4][3]=="1" : #同步於if data[1][1]=="1"意思
            data[4][3]="0"
            data[3][3]="1"
            for a05 in range(0,5,1) :
                for b05 in range(0,6,1) :
                    print(data[a05][b05],end="\t")
                print()
        elif data[3][3]=="1" : #同步於if data[1][1]=="1"意思
            data[3][3]="0"
            data[2][3]="1"
            for a06 in range(0,5,1) :
                for b06 in range(0,6,1) :
                    print(data[a06][b06],end="\t")
                print()
        elif data[2][3]=="1" : #同步於if data[1][1]=="1"意思
            data[2][3]="0"
            data[1][3]="1"
            for a07 in range(0,5,1) :
                for b07 in range(0,6,1) :
                    print(data[a07][b07],end="\t")
                print()
        elif data[1][3]=="1" : #同步於if data[1][1]=="1"意思
            data[1][3]="0"
            data[0][3]="1"
            for a08 in range(0,5,1) :
                for b08 in range(0,6,1) :
                    print(data[a08][b08],end="\t")
                print()
        elif data[1][5]=="1" : #同步於if data[1][1]=="1"意思
            data[1][5]="0"
            data[0][5]="1"
            for a09 in range(0,5,1) :
                for b09 in range(0,6,1) :
                    print(data[a09][b09],end="\t")
                print()
        elif data[2][5]=="1" : #同步於if data[1][1]=="1"意思
            data[2][5]="0"
            data[1][5]="1"
            for a10 in range(0,5,1) :
                for b10 in range(0,6,1) :
                    print(data[a10][b10],end="\t")
                print()
        elif data[3][5]=="1" : #同步於if data[1][1]=="1"意思
            data[3][5]="0"
            data[2][5]="1"
            for a11 in range(0,5,1) :
                for b11 in range(0,6,1) :
                    print(data[a11][b11],end="\t")
                print()
        else : #來到這裡代表,上述可以往上的都找過了但是都沒有找到"1",所以來到這進入
            print("往上走就碰壁啦!")
            for a12 in range(0,5,1) :
                for b12 in range(0,6,1) :
                    print(data[a12][b12],end="\t")
                print()
    elif n==4 : #如果n為4代表往下,是4就進入
        if data[0][1]=="1" : #看目前"1"的位置,此條件式是找可以往下循環的高幾值幾陣列(1個1個找)
            data[0][1]="0" #目前位置先歸"0"
            data[1][1]="1" #然後往下就是高1值1可行走之地方,在設置為"1"
            for e01 in range(0,5,1) : #設置完用for e01跟r01去列印顯示目前模樣
                for r01 in range(0,6,1) :
                    print(data[e01][r01],end="\t")
                print()
        elif data[1][1]=="1" : #同步於if data[0][1]=="1"意思
            data[1][1]="0"
            data[2][1]="1"
            for e02 in range(0,5,1) :
                for r02 in range(0,6,1) :
                    print(data[e02][r02],end="\t")
                print()    
        elif data[2][1]=="1" : #同步於if data[0][1]=="1"意思
            data[2][1]="0"
            data[3][1]="1"
            for e03 in range(0,5,1) :
                for r03 in range(0,6,1) :
                    print(data[e03][r03],end="\t")
                print()
        elif data[3][1]=="1" : #同步於if data[0][1]=="1"意思
            data[3][1]="0"
            data[4][1]="1"
            for e04 in range(0,5,1) :
                for r04 in range(0,6,1) :
                    print(data[e04][r04],end="\t")
                print()
        elif data[0][3]=="1" : #同步於if data[0][1]=="1"意思
            data[0][3]="0"
            data[1][3]="1"
            for e05 in range(0,5,1) :
                for r05 in range(0,6,1) :
                    print(data[e05][r05],end="\t")
                print()
        elif data[1][3]=="1" : #同步於if data[0][1]=="1"意思
            data[1][3]="0"
            data[2][3]="1"
            for e06 in range(0,5,1) :
                for r06 in range(0,6,1) :
                    print(data[e06][r06],end="\t")
                print()
        elif data[2][3]=="1" : #同步於if data[0][1]=="1"意思
            data[2][3]="0"
            data[3][3]="1"
            for e07 in range(0,5,1) :
                for r07 in range(0,6,1) :
                    print(data[e07][r07],end="\t")
                print()
        elif data[3][3]=="1" : #同步於if data[0][1]=="1"意思
            data[3][3]="0"
            data[4][3]="1"
            for e08 in range(0,5,1) :
                for r08 in range(0,6,1) :
                    print(data[e08][r08],end="\t")
                print()
        elif data[0][5]=="1" : #同步於if data[0][1]=="1"意思
            data[0][5]="0"
            data[1][5]="1"
            for e09 in range(0,5,1) :
                for r09 in range(0,6,1) :
                    print(data[e09][r09],end="\t")
                print()
        elif data[1][5]=="1" : #同步於if data[0][1]=="1"意思
            data[1][5]="0"
            data[2][5]="1"
            for e10 in range(0,5,1) :
                for r10 in range(0,6,1) :
                    print(data[e10][r10],end="\t")
                print()
        elif data[2][5]=="1" : #同步於if data[0][1]=="1"意思
            data[2][5]="0"
            data[3][5]="1"
            for e11 in range(0,5,1) :
                for r11 in range(0,6,1) :
                    print(data[e11][r11],end="\t")
                print()
        elif data[3][5]=="1" : #同步於if data[0][1]=="1"意思
            data[3][5]="0"
            data[4][5]="1"
            for e12 in range(0,5,1) :
                for r12 in range(0,6,1) :
                    print(data[e12][r12],end="\t")
                print()
        else : #來到這裡代表,上述可以往下的都找過了但是都沒有找到"1",所以來到這進入
            print("往下走就碰壁啦!")
            for e13 in range(0,5,1) :
                for r13 in range(0,6,1) :
                    print(data[e13][r13],end="\t")
                print()
    if data[4][5]=="1" : #每一輪不管移動左 右 上還是下,都會做最後審查,看是不是目前來到我data裡的高4值5位置值為"1",是就進去,代表結束此迷宮!
        print("已完成迷宮!") #列印已完成迷宮!
        z=False #這時候z做生成值,把它變成False,之後再循環回去while迴圈就不會符合條件式
                #然後不會繼續接下來做新的一輪的由上至下循環,代表結束此while

#迷宮二維陣列模樣    0為可行走步數 4為障礙物不可走 1為自己
#1 0 4 0 0 0
#4 0 4 0 4 0
#4 0 4 0 4 0
#4 0 4 0 4 0
#4 0 0 0 4 0
#高5(高4+高0)值6(值5+值0)

#注意1: 輸入數字1為往左 2為往右 3為往上 4為往下