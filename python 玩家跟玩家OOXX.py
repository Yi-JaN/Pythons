import random
data=[["","",""], #由data二維陣列設計OOXX棋盤格,高3值3(高為 高0 高1 高2) (值為 值0 值1 值2)
      ["","",""],
      ["","",""]]
#summ=0
total=random.randint(1,2) #total為前者跟後者誰是O誰是X
if total==1 : #1的話為
    print("前者為O 後者為X") #前者為0 後者為X
elif total==2 : #2的話為
    print("前者為X 後者為O") #前者為X 後者為O   
z=True #用布林代數去跑,z給True(是)
while z : #while條件式放z,當z還是True(是)時,就會一直循環,當z變False(否)時,回到這裡時該while就無法循環
    n=int(input("1左上/2中上/3右上/4左中/5中間/6右中/7左下/8中下/9右下: ")) #先的人先輸入1-9
    if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9 : #如果是1-9其中1個就進入
        if n==1 and total==1 : #如果輸入為1 而剛剛total是1,代表1(左上)為O
            if data[0][0]=="" : #進入後先看該左上位置是否為空字串,空的才能進去
                data[0][0]="O" #進去後data高0值0位置給為O
             #   summ+=1 
                for i1 in range(0,3,1) : #這邊是列印棋盤格,看當前棋盤格情況
                    for j1 in range(0,3,1) :
                        print(data[i1][j1],end="\t")
                    print() 
        elif n==1 and total==2 : #其他如果輸入為1 而剛剛total是2,代表1(左上)為X
            if data[0][0]=="" : #進入後先看該左上位置是否為空字串,空的才能進去
                data[0][0]="X" #進去後data高0值0位置為X
             #   summ+=1
                for i11 in range(0,3,1) : #這邊是列印棋盤格,看當前棋盤格情況
                    for j11 in range(0,3,1) :
                        print(data[i11][j11],end="\t")
                    print()
        elif n==2 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[0][1]=="" :
                data[0][1]="O"
             #   summ+=1
                for i2 in range(0,3,1) :
                    for j2 in range(0,3,1) :
                        print(data[i2][j2],end="\t")
                    print()
        elif n==2 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[0][1]=="" :
                data[0][1]="X"
             #   summ+=1
                for i22 in range(0,3,1) :
                    for j22 in range(0,3,1) :
                        print(data[i22][j22],end="\t")
                    print()
        elif n==3 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[0][2]=="" :
                data[0][2]="O"
             #   summ+=1
                for i3 in range(0,3,1) :
                    for j3 in range(0,3,1) :
                        print(data[i3][j3],end="\t")
                    print()
        elif n==3 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[0][2]=="" :
                data[0][2]="X"
             #   summ+=1
                for i33 in range(0,3,1) :
                    for j33 in range(0,3,1) :
                        print(data[i33][j33],end="\t")
                    print()
        elif n==4 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[1][0]=="" :
                data[1][0]="O"
             #  summ+=1
                for i4 in range(0,3,1) :
                    for j4 in range(0,3,1) :
                        print(data[i4][j4],end="\t")
                    print()
        elif n==4 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[1][0]=="" :
                data[1][0]="X"
            #    summ+=1
                for i44 in range(0,3,1) :
                    for j44 in range(0,3,1) :
                        print(data[i44][j44],end="\t")
                    print()
        elif n==5 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[1][1]=="" :
                data[1][1]="O"
             #   summ+=1
                for i5 in range(0,3,1) :
                    for j5 in range(0,3,1) :
                        print(data[i5][j5],end="\t")
                    print()
        elif n==5 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[1][1]=="" :
                data[1][1]="X"
             #   summ+=1
                for i55 in range(0,3,1) :
                    for j55 in range(0,3,1) :
                        print(data[i55][j55],end="\t")
                    print()
        elif n==6 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[1][2]=="" :
                data[1][2]="O"
             #   summ+=1
                for i6 in range(0,3,1) :
                    for j6 in range(0,3,1) :
                        print(data[i6][j6],end="\t")
                    print()
        elif n==6 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[1][2]=="" :
                data[1][2]="X"
            #    summ+=1
                for i66 in range(0,3,1) :
                    for j66 in range(0,3,1) :
                        print(data[i66][j66],end="\t")
                    print()
        elif n==7 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[2][0]=="" :
                data[2][0]="O"
             #   summ+=1
                for i7 in range(0,3,1) :
                    for j7 in range(0,3,1) :
                        print(data[i7][j7],end="\t")
                    print()
        elif n==7 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[2][0]=="" :
                data[2][0]="X"
             #   summ+=1
                for i77 in range(0,3,1) :
                    for j77 in range(0,3,1) :
                        print(data[i77][j77],end="\t")
                    print()
        elif n==8 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[2][1]=="" :
                data[2][1]="O"
             #   summ+=1
                for i8 in range(0,3,1) :
                    for j8 in range(0,3,1) :
                        print(data[i8][j8],end="\t")
                    print()
        elif n==8 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[2][1]=="" :
                data[2][1]="X"
              #  summ+=1
                for i88 in range(0,3,1) :
                    for j88 in range(0,3,1) :
                        print(data[i88][j88],end="\t")
                    print()
        elif n==9 and total==1 : #詳情請看上方 if n==1 and total==1 :
            if data[2][2]=="" :
                data[2][2]="O"
             #   summ+=1
                for i9 in range(0,3,1) :
                    for j9 in range(0,3,1) :
                        print(data[i9][j9],end="\t")
                    print()
        elif n==9 and total==2 : #詳情請看上方 elif n==1 and total==2 :
            if data[2][2]=="" :
                data[2][2]="X"
             #   summ+=1
                for i99 in range(0,3,1) :
                    for j99 in range(0,3,1) :
                        print(data[i99][j99],end="\t")
                    print()
        if data[0][0]=="O" and data[0][1]=="O" and data[0][2]=="O" : #來到這邊,先的人輸入完成後,就來到這邊判斷是否連線
           print("O獲勝")                                            #OOXX不管O還是X都各有8種連線方式,然後就開始從這裡一個一個去查
           z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][0]=="X" and data[0][1]=="X" and data[0][2]=="X" :
           print("X獲勝")
           z=False #如果查到就變False,代表連線,不用再跑了
        elif data[1][0]=="O" and data[1][1]=="O" and data[1][2]=="O" :
           print("O獲勝")
           z=False #如果查到就變False,代表連線,不用再跑了
        elif data[1][0]=="X" and data[1][1]=="X" and data[1][2]=="X" :
           print("X獲勝")
           z=False #如果查到就變False,代表連線,不用再跑了
        elif data[2][0]=="O" and data[2][1]=="O" and data[2][2]=="O" :
           print("O獲勝")
           z=False #如果查到就變False,代表連線,不用再跑了
        elif data[2][0]=="X" and data[2][1]=="X" and data[2][2]=="X" :
           print("X獲勝")
           z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][0]=="O" and data[1][0]=="O" and data[2][0]=="O" :
            print("O獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][0]=="X" and data[1][0]=="X" and data[2][0]=="X" :
            print("X獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][1]=="O" and data[1][1]=="O" and data[2][1]=="O" :
            print("O獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][1]=="X" and data[1][1]=="X" and data[2][1]=="X" :
            print("X獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][2]=="O" and data[1][2]=="O" and data[2][2]=="O" :
            print("O獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][2]=="X" and data[1][2]=="X" and data[2][2]=="X" :
            print("X獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][0]=="O" and data[1][1]=="O" and data[2][2]=="O" :
            print("O獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][0]=="X" and data[1][1]=="X" and data[2][2]=="X" :
            print("X獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][2]=="O" and data[1][1]=="O" and data[2][0]=="O" :
            print("O獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        elif data[0][2]=="X" and data[1][1]=="X" and data[2][0]=="X" :
            print("X獲勝")
            z=False #如果查到就變False,代表連線,不用再跑了
        if z==True : #這裡是假設上方先的人都沒查到,接下來換後的人OOXX,阿如果查到了,因為z剛剛變False了,所以這裡就無法成立,這樣就無法進入,後的人也不用OOXX了
            w=int(input("1左上/2中上/3右上/4左中/5中間/6右中/7左下/8中下/9右下: ")) #後的人輸入1-9
            if w==1 or w==2 or w==3 or w==4 or w==5 or w==6 or w==7 or w==8 or w==9 : #如果是1-9其中1個就進入
                if w==1 and total==1 : #如果是輸入1 而剛剛total是1,代表1(左上)為X
                   if data[0][0]=="" : #但是前提是必須為空字串,不然就是先的人沒輸入過這裡,所以一定要為空字串,空的才能進去
                        data[0][0]="X" #進去後data高0值0位置為X
                      #  summ+=1
                        for x1 in range(0,3,1) : #這裡為列印棋盤格,查看當前情況
                            for y1 in range(0,3,1) :
                                print(data[x1][y1],end="\t")
                            print()
                elif w==1 and total==2 : #如果是輸入為1 而剛剛total是2,代表1(左上)為O
                    if data[0][0]=="" : #但是前提是必須為空字串,不然就是先的人沒輸入過這裡,所以一定要為空字串,空的才能進去
                        data[0][0]="O" #進去後data高0值0位置為O
                     #   summ+=1
                        for x11 in range(0,3,1) : #這裡為列印棋盤格,查看當前情況
                            for y11 in range(0,3,1) :
                                print(data[x11][y11],end="\t")
                            print()
                elif w==2 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[0][1]=="" :
                        data[0][1]="X"
                     #   summ+=1
                        for x2 in range(0,3,1) :
                            for y2 in range(0,3,1) :
                                print(data[x2][y2],end="\t")
                            print()
                elif w==2 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[0][1]=="" :
                        data[0][1]="O"
                     #   summ+=1
                        for x22 in range(0,3,1) :
                            for y22 in range(0,3,1) :
                                print(data[x22][y22],end="\t")
                            print()
                elif w==3 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[0][2]=="" :
                        data[0][2]="X"
                    #    summ+=1
                        for x3 in range(0,3,1) :
                            for y3 in range(0,3,1) :
                                print(data[x3][y3],end="\t")
                            print()            
                elif w==3 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[0][2]=="" :
                        data[0][2]="O"
                    #    summ+=1
                        for x33 in range(0,3,1) :
                            for y33 in range(0,3,1) :
                                print(data[x33][y33],end="\t")
                            print()
                elif w==4 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[1][0]=="" :
                        data[1][0]="X"
                     #   summ+=1
                        for x4 in range(0,3,1) :
                            for y4 in range(0,3,1) :
                                print(data[x4][y4],end="\t")
                            print()
                elif w==4 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[1][0]=="" :
                        data[1][0]="O"
                    #    summ+=1
                        for x44 in range(0,3,1) :
                            for y44 in range(0,3,1) :
                                print(data[x44][y44],end="\t")
                            print()
                elif w==5 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[1][1]=="" :
                        data[1][1]="X"
                     #   summ+=1
                        for x5 in range(0,3,1) :
                            for y5 in range(0,3,1) :
                                print(data[x5][y5],end="\t")
                            print()
                elif w==5 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[1][1]=="" :
                        data[1][1]="O"
                     #   summ+=1
                        for x55 in range(0,3,1) :
                            for y55 in range(0,3,1) :
                                print(data[x55][y55],end="\t")
                            print()
                elif w==6 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[1][2]=="" :
                        data[1][2]="X"
                    #    summ+=1
                        for x6 in range(0,3,1) :
                            for y6 in range(0,3,1) :
                                print(data[x6][y6],end="\t")
                            print()            
                elif w==6 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[1][2]=="" :
                        data[1][2]="O"
                     #   summ+=1
                        for x66 in range(0,3,1) :
                            for y66 in range(0,3,1) :
                                print(data[x66][y66],end="\t")
                            print()
                elif w==7 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[2][0]=="" :
                        data[2][0]="X"
                     #   summ+=1
                        for x7 in range(0,3,1) :
                            for y7 in range(0,3,1) :
                                print(data[x7][y7],end="\t")
                            print()
                elif w==7 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[2][0]=="" :
                        data[2][0]="O"
                     #   summ+=1
                        for x77 in range(0,3,1) :
                            for y77 in range(0,3,1) :
                                print(data[x77][y77],end="\t")
                            print()
                elif w==8 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[2][1]=="" :
                        data[2][1]="X"
                     #   summ+=1
                        for x8 in range(0,3,1) :
                            for y8 in range(0,3,1) :
                                print(data[x8][y8],end="\t")
                            print()
                elif w==8 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[2][1]=="" :
                        data[2][1]="O"
                     #   summ+=1
                        for x88 in range(0,3,1) :
                            for y88 in range(0,3,1) :
                                print(data[x88][y88],end="\t")
                            print()
                elif w==9 and total==1 : #詳情請看上方 if w==1 and total==1 :
                    if data[2][2]=="" :
                        data[2][2]="X"
                     #   summ+=1
                        for x9 in range(0,3,1) :
                            for y9 in range(0,3,1) :
                                print(data[x9][y9],end="\t")
                            print()
                elif w==9 and total==2 : #詳情請看上方 elif w==1 and total==2 :
                    if data[2][2]=="" :
                        data[2][2]="O"
                     #   summ+=1
                        for x99 in range(0,3,1) :
                            for y99 in range(0,3,1) :
                                print(data[x99][y99],end="\t")
                            print()
                if data[0][0]=="O" and data[0][1]=="O" and data[0][2]=="O" : #來到這邊,後的人也輸入完成後,就來到這邊判斷是否連線
                   print("O獲勝")                                            #OOXX不管O或X都各有8種連線方式,然後就從這裡一個一個去找
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][0]=="X" and data[0][1]=="X" and data[0][2]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[1][0]=="O" and data[1][1]=="O" and data[1][2]=="O" :
                   print("O獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[1][0]=="X" and data[1][1]=="X" and data[1][2]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[2][0]=="O" and data[2][1]=="O" and data[2][2]=="O" :
                   print("O獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[2][0]=="X" and data[2][1]=="X" and data[2][2]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][0]=="O" and data[1][0]=="O" and data[2][0]=="O" :
                   print("O獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][0]=="X" and data[1][0]=="X" and data[2][0]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][1]=="O" and data[1][1]=="O" and data[2][1]=="O" :
                   print("O獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][1]=="X" and data[1][1]=="X" and data[2][1]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][2]=="O" and data[1][2]=="O" and data[2][2]=="O" :
                   print("O獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][2]=="X" and data[1][2]=="X" and data[2][2]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][0]=="O" and data[1][1]=="O" and data[2][2]=="O" :
                   print("O獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][0]=="X" and data[1][1]=="X" and data[2][2]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][2]=="O" and data[1][1]=="O" and data[2][0]=="O" :
                   print("O獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止
                elif data[0][2]=="X" and data[1][1]=="X" and data[2][0]=="X" :
                   print("X獲勝")
                   z=False #後的人查到後,z就變False,所以先的人不用在出了,因為while代表已停止

#玩法介紹:玩家跟玩家決定好誰先誰後,決定好之後再由先的人執行程式,當跑出前者為O 後者為X
#         意思就是先的人為O 後的人為X,如果是前者為X 後者為O,意思是先的人為X 後的人為O
#         只會用到鍵盤1-9,別案到其他,如果按到其他,不然就是該棋盤格上面已經有O或X,
#         你還執意去輸入的話,會喪失一次機會!