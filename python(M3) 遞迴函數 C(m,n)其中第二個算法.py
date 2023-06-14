def C(x,y) : #函數名稱對函數名稱 x為m y為n
    alls1=1  #在這第一步先設alls1 alls2 alls3,alls1是負責算第一個for i迴圈的層階,像下方公式裡的m!
    alls2=1 #alls2是負責算第二個for j迴圈的層階,像下方公式裡的n!
    alls3=1 #alls3是負責算第三個for k迴圈的層階,像下方公式裡的(m-n!)
    answers=0 #接下來設一個answers為0,answers是負責公式算出來的總和
    for i in range(1,(x+1),1) : #for i算下方公式的m!,for i從1開始 1<x+1 每循環1次+1
        alls1*=i #每循環1次alls1去*目前的i
    for j in range(1,(y+1),1) : #for j算下方公式的n!,for j從1開始 1<y+1 每循環1次+1
        alls2*=j #每循環1次alls2去*目前的j
    for k in range(1,(x-y)+1,1) : #for k算下方公式的(m-n!),for k從1開始 1<(x-y)+1 每循環1次+1
        alls3*=k #每循環1次alls3去*目前的k
    answers=(alls1)//((alls2)*(alls3)) #answers負責利用公式算出來的總和    
    return answers #來到這再把answers的答案回傳,回傳到當初由下至上函數名稱對函數名稱的那個print括號裡
                   #那answers沒下函數名稱就直接回傳,所以回傳回去後,該值不能再丟上來這做遞迴函數  

m=int(input()) #輸入整數給m
n=int(input()) #輸入整數給n
print(C(m,n)) #接下來把m跟n丟到函數名稱C裡面,接著函數名稱對函數名稱由下至上進去def函數裡

#C(m,n)公式如下:
#C(m,n)=m!/(n!(m-n!))

#輸入->m=8   m=5
#輸入->n=6   n=4
#輸出->28      5