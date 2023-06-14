#陣列行列互換
data=[[0]*7 for o in range(5)] #輸入一個二維陣列取我輸入的值,[0]*7代表取7個值(從0開始) for o in range(5)取5個高(從高0開始)
for i in range(0,5,1) : #一開始先data二維陣列取高5值7的值,for i為高
    for j in range(0,7,1) :  #for j為值
        data[i][j]=int(input()) #用我所輸入的正整數一個一個值慢慢取! 這時候全部取完,data二維陣列跟下方python5*7表示一模一樣
for a in range(0,7,1) : #這邊開始把我取的值從高5值7變高7值5,另外for a先假設為高
    for b in range(0,5,1) : #for b先假設為值
        print(data[b][a],end="\t") #重點是這行,把我取到的高(a)跟值(b)互換,變成data[b][a],然後data原本就有取正整數
    print()                        #值了,所以把我有data正整數值依照data[b][a]方式"變成data裡的正整數取值方式變成側翼取值"
  #上面這print()是每列完一行來到這邊換行,繼續做下一行列印,之後返回for a以此類推循環
  
#補充:側翼取值是像題目裡的81 90 9 28 5這行就是側翼,再來繼續取7 67 54 8 1,以此類推取側翼
#補充:用end="\t"是因為每一列每個值看起來比較整齊
#補充:列數高意思是"這個高的數字值"     
#下方為範例題目:
#81  7   7   10  97  0   97  <-第1高 (高0)
#90  67  8   25  1   39  34  <-第2高 (高1)
#9   54  63  53  53  55  77  <-第3高 (高2)
#28  8   17  50  41  99  89  <-第4高 (高3)
#5   1   95  99  76  92  60  <-第5高 (高4)
#上述二維陣列在python裡5*7表示是這樣表示如下":
# [[81,7,7,10,97,0,97],[90,67,8,25,1,39,34],[9,54,63,53,53,55,77],
#  [28,8,17,50,41,99,89],[5,1,95,99,76,92,60]]
#
#範例題目答案如下:
#81	90	9	28	5	
#7	67	54	8	1	
#7	8	63	17	95	
#10	25	53	50	99	
#97	1	53	41	76	
#0	39	55	99	92	
#97	34	77	89	60	

#上方範例題目答案側翼取值如下:
#                       b   a        b  a        b  a        b  a        b  a
#        圖像->  (81)   0   0  (90)  1   0  (9)  2   0  (28) 3   0  (5)  4   0
#                (7)   0   1  (67)  1   1  (54)  2   1  (8)  3   1  (1)  4   1
#                (7)   0   2  (8)   1   2  (63)  2   2  (17) 3   2  (95) 4   2
#                (10)  0   3  (25)  1   3  (53)  2   3  (50) 3   3  (99) 4   3
#             之後答案下面的列數高是一模一樣取"側翼"的算法演練
