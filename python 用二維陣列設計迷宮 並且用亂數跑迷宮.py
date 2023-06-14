import random
data=[[1,0,4,0,0,0], #高0   #data為二維陣列,5x6->有加高0跟值0
      [4,0,4,0,4,0], #高1
      [4,0,4,0,4,0], #高2
      [4,0,4,0,4,0], #高3
      [4,0,0,0,4,3]] #高4
z1=True #z1先設布林數True用來使用第一個while迴圈循環
z2=True #z2先設布林數True用來使用第二個while迴圈循環
run1=0
run2=0
count=0 #count為計數,先設為0,用來取亂數行走次數
i=0 #i為記錄使用者玩家的目前步數
j=0 #j是處理刪除i要移動到下一步數前的目前此步數的正整數1
k=0 #k為記錄目前此i值的步數,並且控制亂數產生移動步數時能到達終點,不超出
while z1 : #z1是為了讓while迴圈持續循環,當z1為False此while就不循環了
    run1=random.randint(0,4) #進去輸入一個run1,讓他產生0到4亂數正整數值
    count+=1 #每循環1次,count計數+1,不管是亂數產生0 1 2 3 4
    i+=run1 #i+現在的亂數產生步數
    if i==1 : #如果i是1
        data[0][1]=1 #針對1的步數,找出他位於的二維陣列地方,然後針對此地方做生成值
        data[0][0]=2 #起點的位置就恢復為2
        for i1 in range(0,5,1) : #for i1為高,這裡開始列印二維陣列地圖
            for j1 in range(0,6,1) :# for j1為值
                print(data[i1][j1],end=" ") #每循環1次列印目前的data[i1]高[j1]值的位置值出來,並且在空格
            print() #一個二維陣列的高結束後,就換行,換下一行列印       
        z1=False #z1就變為False,代表此while不繼續循環
    elif i==2 : #i==2 跟i==3跟i==4都跟i==1是一樣的意思
        data[1][1]=1 #i==2位於的二維陣列地方是高1值1位置
        data[0][0]=2
        for i2 in range(0,5,1) :
            for j2 in range(0,6,1) :
                print(data[i2][j2],end=" ")
            print()    
        z1=False
    elif i==3 :
        data[2][1]=1 #i==3位於的二維陣列地方是高2值1位置
        data[0][0]=2
        for i3 in range(0,5,1) :
            for j3 in range(0,6,1) :
                print(data[i3][j3],end=" ")
            print()    
        z1=False
    elif i==4 :
        data[3][1]=1 #i==4位於的二維陣列地方是高3值1位置
        data[0][0]=2
        for i4 in range(0,5,1) :
            for j4 in range(0,6,1) :
                print(data[i4][j4],end=" ")
            print()    
        z1=False
    elif i==0 : #如果是0的話代表還在起點,在起點的話繼續循環while迴圈
        for i0 in range(0,5,1) : #列印二維陣列地圖
            for j0 in range(0,6,1) :
                print(data[i0][j0],end=" ")
            print()
        print() #因為是0所以還會繼續循環while,所以這邊自己提前在換行,跟下一個地圖陣列有個距離    
print()        
while z2 : #z2是為了讓while迴圈持續循環,當z2為False此while就不循環了
    k=i #每循環第一步是先看當前i的步數,然後當前i的步數丟給k檢查
    if  k==14 or k==15 or k==16 : #檢查當前步數,如果步數為14到16則進
        if k==14 : #14進去
            run2=random.randint(0,3) #控制目前步數產生,只產生0到3
        elif k==15 : #15進去
            run2=random.randint(0,2) #控制目前步數產生,只產生0到2
        elif k==16 : #16進去
            run2=random.randint(0,1) #控制目前步數產生,只產生0到1
    else :
        run2=random.randint(0,4) #只要不是目前步數是14 15 16就正常亂數產生
    count+=1 #每循環產生步數後,就count計數+1
    j=i #要移動到下一步數前,先把目前此步數丟給j移除
    if j==1 : #j是1
       data[0][1]=0 #針對目前此步數位於的二維陣列高0值1位置值汰舊換新變為0
    elif j==2 :
       data[1][1]=0 #2位於的二維陣列位置為高1值1
    elif j==3 :
       data[2][1]=0 #3位於的二維陣列位置為高2值1
    elif j==4 :
        data[3][1]=0 #4位於的二維陣列位置為高3值1
    elif j==5 :
        data[4][1]=0 #5位於的二維陣列位置為高4值1
    elif j==6 :
        data[4][2]=0 #6位於的二維陣列位置為高4值2
    elif j==7 :
        data[4][3]=0 #7位於的二維陣列位置為高4值3
    elif j==8 :
        data[3][3]=0 #8位於的二維陣列位置為高3值3
    elif j==9 :
        data[2][3]=0 #9位於的二維陣列位置為高2值3
    elif j==10 :
        data[1][3]=0 #10位於的二維陣列位置為高1值3
    elif j==11 :
        data[0][3]=0 #11位於的二維陣列位置為高0值3
    elif j==12 :
        data[0][4]=0 #12位於的二維陣列位置為高0值4
    elif j==13 :
        data[0][5]=0 #13位於的二維陣列位置為高0值5
    elif j==14 :
        data[1][5]=0 #14位於的二維陣列位置為高1值5
    elif j==15 :
        data[2][5]=0 #15位於的二維陣列位置為高2值5
    elif j==16 :
        data[3][5]=0 #16位於的二維陣列位置為高3值5
    i+=run2 #之後開始移動到下一步,(i+剛剛亂數產生的(run2)值)
    if i==17 : #移動到下一步數後如果是17進去
        data[4][5]=1 #17位於的二維陣列位置為高4值5,所以data高4值5的位置做生成值
        for x in range(0,5,1) : #for x為高,這裡開始列印二維陣列地圖
            for y in range(0,6,1) : #for y為值
                print(data[x][y],end=" ") #每循環1次列印目前的data[x]高[y]值的位置值出來,並且在空格
            print() #一個二維陣列的高結束後,就換行,換下一行列印 
        z2=False #17為終點,z2就為False,結束此while迴圈循環
    elif i>=1 and i<=16 : #如果是1到16則進去
        if i==1 :
          data[0][1]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,1位置值為高0值1
          for x in range(0,5,1) : #for x為高,這裡開始列印二維陣列地圖
              for y in range(0,6,1) : #for y為值
                  print(data[x][y],end=" ") #每循環1次列印目前的data[x]高[y]值的位置值出來,並且在空格
              print() #一個二維陣列的高結束後,就換行,換下一行列印   
        elif i==2 :
          data[1][1]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,2位置值為高1值1
          for x in range(0,5,1) : #for x為高,這裡開始列印二維陣列地圖
              for y in range(0,6,1) : #for y為值
                  print(data[x][y],end=" ") #每循環1次列印目前的data[x]高[y]值的位置值出來,並且在空格
              print() #一個二維陣列的高結束後,就換行,換下一行列印 
        elif i==3 :
          data[2][1]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,3位置值為高2值1
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()    
        elif i==4 :
          data[3][1]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,4位置值為高3值1
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==5 :
          data[4][1]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,5位置值為高4值1
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==6 :
          data[4][2]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,6位置值為高4值2
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==7 :
          data[4][3]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,7位置值為高4值3
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==8 :
          data[3][3]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,8位置值為高3值3
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==9 :
          data[2][3]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,9位置值為高2值3
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==10 :
          data[1][3]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,10位置值為高1值3
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==11 :
          data[0][3]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,11位置值為高0值3
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==12 :
          data[0][4]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,12位置值為高0值4
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==13 :
          data[0][5]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,13位置值為高0值5
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==14 :
          data[1][5]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,14位置值為高1值5
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==15 :
          data[2][5]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,15位置值為高2值5
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
        elif i==16 :
          data[3][5]=1 #+完下一步後,針對目前此i值步數位於的二維陣列做生成值為1,16位置值為高3值5
          for x in range(0,5,1) :
              for y in range(0,6,1) :
                  print(data[x][y],end=" ")
              print()
    print() #此print()是列印二維陣列地圖後,再列印下一次時彼此之間距離離一行          
print("共行走亂數迷宮次數為:",count,"次!")

#二維陣列地圖如下 : 5x6
#[[1,0,4,0,0,0], #高0  #介紹: 2為起點初始地(高0值0),一開始使用者會在此地方做為起點,而一開始還沒動時2不是2
# [4,0,4,0,4,0], #高1         而是1,因為一開始使用者在這,所以使用者數字(1)會先蓋過2,等到1開始移動後,起點
# [4,0,4,0,4,0], #高2         初始地就會從1變成2
# [4,0,4,0,4,0], #高3         1設為使用者自己
# [4,0,0,0,4,3]] #高4         0為可行走區域,4為不可走區域,3為最後終點(終點設在高4值5)

#第一個while迴圈->第一個while迴圈功用是先讓使用者先離開起點初始地,等到離開初始地後,起點初始地變成2
#                之後因為使用者已離開起點初始地,所以第一個while迴圈工作就結束,換第二個while迴圈循環跑迷宮 