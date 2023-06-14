#水果平台簡易銷售
import math  #設這個math是要用math.floor
str11="水果平台簡易銷售"
print("*********",str11,"*********")
print("注意事項: 蘋果消費滿550 香蕉消費滿450 梨子消費滿420 打85折")
print("售價*1 (1.)蘋果:45元 (2.)香蕉:35元 (3.)梨子:32元")
number=int(input("請輸入水果編號: "))
number2=int(input("請輸入該水果購買數量: "))
money1=number2*45   #先把購買數量計算到全部的水果上,之後待會對應水果編號再丟水果
money2=number2*35   #變數名稱裡的價錢 money1是蘋果 money2是香蕉 money3是梨子
money3=number2*32
if number==1 :  #如果是編號1就進去
    if money1>=550 : #進去後就是蘋果的價錢丟進去內圈if判斷有沒有符合打折規範
        allmoney=money1*0.85 #有的話進來內圈if打0.85折
        print(math.floor(allmoney)) #算完用floor把小數點第1位(包含)後面的值通通用掉不4捨五入留整數
    else : #else就是沒有符合打折的
        print(money1) #進去後直接把蘋果錢取過來列印即可
elif number==2 : #elif如果是編號2就進去
     if money2>=450 : #進去後就是香蕉的價錢,丟進去內圈if判斷有沒有符合打折規範
         allmoney=money2*0.85 #有的話進來內圈if打0.85折
         print(math.floor(allmoney)) #算完用floor把小數點第1位(包含)後面的值通通用掉不4捨五入留整數
     else : #else就是沒有符合打折的
         print(money2) #進去後直接把香蕉錢取過來列印即可
elif number==3 : #如果是編號3就進去
     if money3>=420 : #進去後判斷梨子的價錢,丟進去內圈if判斷有沒有符合打折規範
           allmoney=money3*0.85 #有的話進來此內圈if打0.85折
           print(math.floor(allmoney)) #算完用floor把小數點第1位(包含)後面的值通通用掉不4捨五入留整數
     else : #else就是沒有符合打折的
           print(money3) #進去後直接把梨子錢取過來列印即可
else :  #外圈如果判斷到這行else,代表妳水果編號不是1或2或3,所以直接來到這行顯示錯誤!
    print("水果編號輸入錯誤!")  


#請輸入水果編號: 2         請輸入水果編號: 3
#請輸入水果購買數量: 7     請輸入水果購買數量: 14
#245                      380