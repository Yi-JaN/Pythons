#銀行換鈔票
n=int(input("請換取金額(限於100-30000): ")) #輸入要換鈔金額
ten=(n//10)%10 #此ten是算你換鈔金額的十位數字有沒有數字,如果有不能換,因為鈔票最低為一百,也就是百位數
dollars=(n%10) #此dollars是算你換鈔金額的個位數字有沒有數字,如果有不能換,因為鈔票最低為一百,也就是百位數
thousand=0 #待會換算千元鈔票有幾張
thousands=0 #待會換算換完千元鈔票後還有多少金額
fivehundred=0 #待會把換完千元鈔票後還有多少金額的值換算五百鈔票看有幾張
fivehundreds=0 #待會換完五百鈔票剩下的金額看多少
hundred=0 #待會換完五百鈔票剩下的金額看多少在換算最低的百元鈔,看能換幾張
if n>=100 and n<=30000 : #如果符合100到30000之間就進去
    if n>=100 and n<500 and ten==0 and dollars==0 : #如果金額是100到<500之間然後ten跟dollars==0就進去
        hundred=n//100 #進去就只換百鈔
        print("能換",hundred,"張百鈔")
    elif n>=500 and n<1000 and ten==0 and dollars==0 : #如果金額是500~<1000之間然後ten跟dollars==0就進去
        fivehundred=n//500 #進去先換五百鈔
        fivehundreds=n%500 #換完五百看剩多少錢
        hundred=fivehundreds//100 #把剩下的錢換百元鈔
        print("能換",fivehundred,"張五百鈔")
        print("能換",hundred,"張百鈔")
    elif n>=1000 and n<=30000 and ten==0 and dollars==0 : #如果金額是1000以上到30000然後ten跟dollars==0就進去
        thousand=n//1000 #進去先換千元鈔
        thousands=n%1000 #換完千元鈔看剩多少錢
        fivehundred=thousands//500 #剩下的錢依序換五百鈔
        fivehundreds=thousands%500 #換完五百鈔在看剩多少錢
        hundred=fivehundreds//100 #把換完五百鈔看剩下的錢換成百元鈔
        print("能換",thousand,"張千元鈔")
        print("能換",fivehundred,"張五百鈔")
        print("能換",hundred,"張百鈔")
    elif n>=100 and n<=30000 and ten!=0 and dollars!=0 : #如果你的值是100~30000然後ten跟dollars同時都不等於0那就進去
        print("十位數字和個位數字沒鈔票,最低鈔票為百元鈔") #進去代表你十位跟個位數字有值,最低鈔為百鈔
    elif n>=100 and n<=30000 and ten!=0 : #如果你的值是100~30000然後ten不等於0那就進去
        print("十位數字沒鈔票,最低鈔票為百元鈔") #進去代表你十位數字有值,最低鈔為百鈔
    elif n>=100 and n<=30000 and dollars!=0 : #如果你的值是100~30000然後dollars不等於0那就進去
        print("個位數字沒鈔票,最低鈔票為百元鈔") #進去代表你個位數字有值,最低鈔為百鈔
else :
   print("未在範圍值輸入金額!")        

#銀行換鈔票,輸入一組100-30000之間的數字(超過或低於不算),並且只能換鈔票,而鈔票低至高有
#一百 五百跟一千,看這組數字能換幾張一百 五百跟一千鈔票,注意:如果十位數字跟個位數字有值
#則不能換,因為鈔票最低為100,即使輸入在100-30000以內也一樣

#輸入n->400          800           1200          10800          201
#輸出->能換4張百鈔  能換1張五百鈔  能換1張千元鈔   能換10張千元鈔  個位數字沒鈔票,最低鈔票為百元鈔
#輸出->            能換3張百鈔    能換0張五百鈔   能換1張五百鈔
#輸出->                          能換2張百鈔     能換3張百鈔

#輸入n->635                                        1150                          35000
#輸出->十位數字和個位數字沒鈔票,最低鈔票為百元鈔    十位數字沒鈔票,最低鈔票為百元鈔   未在範圍值輸入金額!