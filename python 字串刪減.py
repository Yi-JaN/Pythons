str1=str(input()) #輸入一組字串
str2="" #待會要拿來1個1個+符合的str1的單字串
a=len(str1) #先算該字串長度
for i in range(0,a,1) : #把長度丟進去for i,正向循環從第一個單字串開始取,第一個單字串位置值為0,所以for i從0開始循環,每循環1次+1
    ch=str1[i] #每循環1次取str1的i位置值單字串給ch去做生成值
    if ch>='A' and ch<='Z' or ch>='a' and ch<='z' or ch>='0' and ch<='9' or ch==' ' : #如果符合此if迴圈外圈條件式就進去
        str2+=ch #進去就加符合該條件式的ch,ch進來會是有大寫 小寫英文字母 數字單字串 空白字串!
str1=str2 #來到這邊代表for i ok,所以str2+起來的總字串值丟給我當初輸入的str1做生成值
print(str1)  #然後列印最終字串刪減的總字串值答案出來

#題目: 字串刪減
#題目說明:輸入一組字串,做此字串的刪減,字串只能留大寫 小寫英文字母 數字單字串 跟空白字串,沒有上述幾種,通通
#        做該字串刪減,例如除了空白字串外的特殊符號字元,就可以做刪減,刪減完最後的總字串值就是答案!

#輸入->ABC.123      #!Hello Python .//Taiwan
#輸出->ABC123       Hello Python Taiwan