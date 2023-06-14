def answer1(x,y) : #函數名稱對函數名稱如果是answer1就進來這邊 x就為n y就為alls
    if x>=1 : #第一步如果x大於等於1就進去
        y+=1 #y就+1
        x=x//10 #x除以10取商數做x的生成值
        return answer1(x,y) #把x跟y再丟回去answer1括號裡,並且return到當初由下至上上來這裡的print括號裡,這裡有下函數名稱
    else :  #如果不是>=1就進去else裡                                  #,有下的話還會再丟上來這def函數裡循環
        return y #直接把y return回去,return回去到當初由下至上上來這裡的print括號裡,這裡沒下函數名稱,所以丟回去的值就不會再丟上來這裡
def answer2(x,y) : #函數名稱對函數名稱如果是answer2就進來這邊 x就為nn y就為allss
    if x>=1 : #第一步如果x大於等於1就進去
        y+=(x%10) #y就+目前該x值的%10餘數
        x=x//10 #x除以10取商數做x的生成值
        return answer2(x,y) #把x跟y再丟回去answer2括號裡,並且return到當初由下至上上來這裡的print括號裡,這裡有下函數名稱
    else : #如果不是>=1就進去else裡                                   #,有下的話還會再丟上來這def函數裡循環
        return y #直接把y return回去,return回去到當初由下至上上來這裡的print括號裡,這裡沒下函數名稱,所以丟回去的值就不會再丟上來這裡

z=True #一開始設布林數True給變數名稱z
while z : #用while迴圈循環,如果z還是True就繼續循環,如果z是False就結束while循環
    x=int(input("計數位數請輸入1,計數總和請輸入2: ")) #第一步就是看你要算位數還是總和,如果是位數輸入1,總和輸入2
    if x==1 or x==2 : #如果輸入是1或2就進去
        if x==1 : #是1的話進去
            n=int(input()) #輸入一個值轉int值給n
            alls=0 #alls為0
            print(answer1(n,alls)) #丟給函數名稱answer1括號裡,待會由下至上,函數名稱對函數名稱對該def函數
        elif x==2 : #是2的話進去
            nn=int(input()) #輸入一個值轉int值給nn
            allss=0 #allss為0
            print(answer2(nn,allss)) #丟給函數名稱answer2括號裡,待會由下至上,函數名稱對函數名稱對該def函數
        z=False #不管是輸入1還2,到最後來到這邊布林數變False給z,待會就停止while迴圈循環   
    else : #如果輸入不是1或2就進去,代表輸入數字錯誤
        print("數字輸入錯誤!") #顯示該字串外,待會還要重新循環while迴圈

#計數位數請輸入1,計數總和請輸入2: 1     計數位數請輸入1,計數總和請輸入2: 2      
#4395                                 4395
#4                                    21
#計數位數請輸入1,計數總和請輸入2: 1     計數位數請輸入1,計數總和請輸入2: 2
#0548                                 0548
#3                                    17

#Python看遞迴是由下至上循環這樣看 Java看遞迴是由上至下循環這樣看