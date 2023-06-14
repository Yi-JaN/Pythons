def lists(n,data) : #函數名稱對函數名稱後, def的n為n二維陣列 def的data為data一維陣列
    a=len(n) #先判斷此二維陣列的高有幾個高
    for i in range(0,a,1) : #for i負責當高,a放進去,二維陣列第1高為高0,所以為0,從高0開始 每循環1次+1
        if i==0 : #i(高)如果是高0(第一個高)就進去
            if n[i][0]<=n[i][1] and n[i][1]<=n[i][2] : #判斷高0裡的3個值的三角形特性,如下方說明的第一點
                if (((n[i][0]*n[i][0])+(n[i][1]*n[i][1]))==(n[i][2]*n[i][2])) : #符合就進入,然後再這行先判斷是否符合如下方說明的第二點!
                    data+=["True"] #是就進去判斷為"True"推給data一維陣列
                else : #第二點不符合就進入
                    data+=["False"] #不符合就進去判斷為"False"推給data一維陣列
            else : #如果第一點不符合就進入
                data+=["False"] #不符合就進去判斷為"False"推給data一維陣列
        elif i%2>0 : #如果i(高)如果是奇數高就進去
            if n[i][0]<=n[i][1] and n[i][1]<=n[i][2] : #判斷奇數高裡的3個值的三角形特性,如下方說明的第一點
                if (((n[i][0]*n[i][0])+(n[i][1]*n[i][1]))==(n[i][2]*n[i][2])) : #符合就進入,然後再這行先判斷是否符合如下方說明的第二點!
                    data+=["True"] #是就進去為"True"推給data一維陣列
                else : #第二點不符合就進入
                    data+=["False"] #不符合就進去判斷為"False"推給data一維陣列
            else : #如果第一點不符合就進入
                data+=["False"] #不符合就進去判斷為"False"推給data一維陣列
        elif i%2==0 : #如果i(高)如果是偶數高就進去
            if n[i][0]<=n[i][1] and n[i][1]<=n[i][2] : #判斷偶數高裡的3個值的三角形特性,如下方說明第一點
                if (((n[i][0]*n[i][0])+(n[i][1]*n[i][1]))==(n[i][2]*n[i][2])) : #符合就進入,然後再這行先判斷是否符合如下方說明的第二點!
                    data+=["True"] #是就進去為"True"推給data一維陣列
                else : #第二點不符合就進入
                    data+=["False"] #不符合就進去判斷為"False"推給data一維陣列
            else : #如果第一點不符合就進入
                data+=["False"] #不符合就進去判斷為"False"推給data一維陣列
    return data    #上述for i以此類推循環後,for i ok之後,來到這邊把最終的data一維陣列回傳回去,並且"不下函數名稱",以免又傳上來def函數名稱對函數名稱        
    
n=[[1,2,3],[3,4,5],[5,12,13],[0,2,3]] #n為一個二維陣列,裡面有4個高,每個高裡面代表是一個待會要判斷的三角形邊長的值,待會先全部丟入函數名稱裡
data=[] #用data一維陣列表示這4個高哪一個是符合True與False要求,根據二維陣列的位置顯現這4個高的判斷出來
print(lists(n,data)) #n跟data一同帶入lists的函數名稱裡,讓他函數名稱對函數名稱由下至上丟上去def遞迴函數

#說明如下:
#一.三角形特性->先判斷3個邊,第1邊 第2邊 第3邊是否都是 1<=2<=3 ,是的話就進去,不是就直接判斷"False"
#二.三角形特性->進去後判斷直角三角形符合特性,直角三角形符合特性是 ((第1邊*第1邊)+(第2邊*第2邊))==(第3邊*第3邊),如果符合上述就是了,不是就直接判斷"False"

#輸出->:['False','True','True','False']    