#輸入一組字串 查此字串大寫和小寫各幾個 數字 空白 特殊字元各幾個
str1=str(input()) #輸入一組字串
countA=0 #查大寫單字串有幾個
counta=0 #查小寫單字串有幾個
count0=0 #查數字單字串有幾個
countspace=0 #查空白單字串有幾個
countelse=0 #查其他特殊字元有幾個
a=len(str1) #找此字串共有幾個值,當做長度值
for i in range(0,a,1) : #用for循環單字串1個1個找,字串第一個單字串必為0,a放進去看循環幾次,就跟著for i取str1單字串的值
    ch=str1[i] #每循環一次就取str1的i位置的單字串值給ch做生成值,讓ch拿到str1的i位置的單字串值
    if ch>='A' and ch<='Z' : #如果ch拿到目前i位置的單字串值,就比看看是不是大寫,是就進入此if迴圈
       countA+=1 #進去之後負責統整大寫單字串數的countA加1
    elif ch>='a' and ch<='z' : #如果此位置的單字串值不是大寫,就往下來這裡比看看是不是小寫,是就進入此if迴圈
       counta+=1 #進去之後負責統整小寫單字串數的counta加1
    elif ch>='0' and ch<='9' : #如果是數字單字串就來這邊
       count0+=1 #進去之後負責統整數字單字串數的count0加1
    elif ch==' ' : #如果再往下是空白單字串就來這邊
       countspace+=1 #進去之後負責統整空白單字串數的countspace加1
    else : #上面if迴圈都不是就來到else這邊,會來到這邊代表目前拿到i位置的單字串值是特殊字元
       countelse+=1 #進去之後負責統整特殊字元單字串數的countelse加1
print("大寫有:",countA,"個") #上述for迴圈以此類推之後,做到for OK之後就來到這邊,開始列印各自找到的統整值
print("小寫有:",counta,"個")
print("數字有:",count0,"個")
print("空白有:",countspace,"個")
print("特殊字元有:",countelse,"個")

#輸入->AbC123#            !#N nBCna20
#輸出->大寫有:2個          大寫有:3個 
#輸出->小寫有:1個          小寫有:3個
#輸出->數字有:3個          數字有:2個
#輸出->空白有:0個          空白有:1個
#輸出->特殊字元有:1個      特殊字元有:2個 
        