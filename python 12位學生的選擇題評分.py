student=[[0]*10 for o in range(12)] #12位學生,每個學生為1個高,共12個高10個值,12x10
score=[] #score一維陣列是待會要給各自學生的總成績置放地方
mm=10 #mm為一題10分,標準答案共10題
summ=0 #此summ是待會要1個1個算學生各自的總分成績
for a in range(0,12,1) : #for a為高為學生數,此for是取12位學生的作答答案
    for b in range(0,10,1) : #for b為值為每個學生的作答
        student[a][b]=str(input()) #每循環一次取1個自己輸入的答案丟至目前的高a值b位置上        
for i in range(0,12,1) : #for i為二維陣列的高為學生數,此for是開始對答案的地方
    for j in range(0,10,1) :#for j為二維陣列的值為每個學生的作答,從0開始循環,也就是從第一題循環到第十題
        if j==0 : #j==0代表為學生作答第一題
            if student[i][j]=='A' : #進去後針對值0的部份(也就是第一題)是A就進去
                summ+=mm #進去後就加總和
        elif j==1 : #j==1代表為學生作答第二題
            if student[i][j]=='C' : #進去後針對值1的部份(也就是第二題)是C就進去
                summ+=mm #進去後就加總和
        elif j==2 : #j==2代表為學生作答第三題
            if student[i][j]=='D' : #進去後針對值2的部份(也就是第三題)是D就進去
                summ+=mm #進去後就加總和
        elif j==3 : #j==3代表為學生作答第四題
            if student[i][j]=='D' : #進去後針對值3的部份(也就是第四題)是D就進去
                summ+=mm #進去後就加總和
        elif j==4 : #j==4代表為學生作答第五題
            if student[i][j]=='B' : #進去後針對值4的部份(也就是第五題)是B就進去
                summ+=mm #進去後就加總和
        elif j==5 : #j==5代表為學生作答第六題
            if student[i][j]=='A' : #進去後針對值5的部份(也就是第六題)是A就進去
                summ+=mm #進去後就加總和
        elif j==6 : #j==6代表為學生作答第七題
            if student[i][j]=='A' : #進去後針對值6的部份(也就是第七題)是A就進去
                summ+=mm #進去後就加總和
        elif j==7 : #j==7代表為學生作答第八題
            if student[i][j]=='C' : #進去後針對值7的部份(也就是第八題)是C就進去
                summ+=mm #進去後就加總和
        elif j==8 : #j==8代表為學生作答第九題
            if student[i][j]=='C' : #進去後針對值8的部份(也就是第九題)是C就進去
                summ+=mm #進去後就加總和
        elif j==9 : #j==9代表為學生作答第十題
            if student[i][j]=='D' : #進去後針對值9的部份(也就是第十題)是D就進去
                summ+=mm #進去後就加總和
    score+=[summ] #把每個高(<-學生)裡的值算出總分後推給score一維陣列置放
    summ=0    #置放完歸0,換取下一個高(<-學生)的成績   
print("學生1為: ",score[0]) #score值0為學生1的總成績
print("學生2為: ",score[1]) #score值1為學生2的總成績
print("學生3為: ",score[2]) #score值2為學生3的總成績
print("學生4為: ",score[3]) #score值3為學生4的總成績
print("學生5為: ",score[4]) #score值4為學生5的總成績
print("學生6為: ",score[5]) #score值5為學生6的總成績
print("學生7為: ",score[6]) #score值6為學生7的總成績
print("學生8為: ",score[7]) #score值7為學生8的總成績
print("學生9為: ",score[8]) #score值8為學生9的總成績
print("學生10為: ",score[9]) #score值9為學生10的總成績
print("學生11為: ",score[10]) #score值10為學生11的總成績
print("學生12為: ",score[11]) #score值11為學生12的總成績

# 標準答案     ACDDBAACCD     總分
#  1          AAAAAAAAAA      30
#  2          BBBBBBBBBB      10
#  3          CCCCCCCCCC      30
#  4          DDDDDDDDDD      30 
#  5          ABCDABCDAB      20
#  6          AABBCCDDAA      10
#  7          AAABBBCCCD      50
#  8          ACDDBAACCD     100  
#  9          ACDDBAACCD     100
# 10          ACDDBAACCD     100    
# 11          ACDDBAAAAA      70
# 12          AAAAAAACCD      60

#請寫出依照上表的學生成績,列印12位學生的總分出來