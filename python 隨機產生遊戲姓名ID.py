import random
AZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #AZ為字串(大寫26個字母)
az="abcdefghijklmnopqrstuvwxyz" #az為字串(小寫26個字母)
number="0123456789" #number為字串(數字單字串0~9)
arrAZ=[] #arrAZ為一維陣列,待會取大寫部份
arraz=[] #arraz為一維陣列,待會取小寫部份
arr09=[] #arr09為一維陣列,待會取數字單字串部份
str1="" #str1一開始為空字串,之後要用str1取得8個單字串結合起來的字串
for i in range(0,1,1) : #for i負責取大寫部份,大寫只有一個,所以從0開始 0<1 每循環1次+1
    ch1=random.choice(AZ) #每循環1次ch1取利用choice去取AZ字串中的其中一個單字串出來
    arrAZ+=[ch1] #取出來的單字串推給arrAZ
for j in range(0,5,1) : #for j負責取小寫部份,小寫為中間部份,有5個,所以從0開始 0<5 每循環1次+1
    ch2=random.choice(az) #每循環1次ch2取利用choice去取az字串中的其中一個單字串出來
    arraz+=[ch2] #取出來的單字串推給arraz
for k in range(0,2,1) : #for k負責取數字部份,數字單字串只有2個,所以從0開始 0<2 每循環1次+1
    ch3=random.choice(number) #每循環1次ch3取利用choice去取number字串中的其中一個單字串出來
    arr09+=[ch3] #取出來的單字串推給arr09
for x in range(0,1,1) : #這邊開始就是組成字串,for x為大寫部份,大寫先(因為大寫為第一個單字串)
    str1+=arrAZ[x] #str1去加arrAZ目前x位置值的單字串
for y in range(0,5,1) : #for y為小寫部份(小寫為中間部份),0<5 每循環1次+1
    str1+=arraz[y] #每循環1次str1去加arraz目前y位置值的單字串
for z in range(0,2,1) : #for z為數字部份(數字為最後部份,倒數第一 第二單字串) 0<2 每循環1次+1    
    str1+=arr09[z] #每循環1次str1去加arr09目前y位置值的單字串
print(str1)    
    

#題目說明: 某遊戲公司想要產生一個隨機產生姓名ID方便給玩家使用,讓玩家不用自己想遊戲ID
#          也能夠利用這個去產生隨機遊戲姓名ID給玩家自己使用,所以此遊戲公司的設計是8
#          個單字串結合起來為一組字串給玩家使用,8個單字串中有大小寫跟數字單字串,所以
#          要設計的話請依照下方規則做設計
#規則    : 需要8個單字串->8個單字串為一組字串->一組字串中第一個單字串為大寫 倒數第一
#         第二個單字串為數字單字串,其餘中間部份為小寫

#範例產生如下:
#Iegrix86   Qbylgt73   Rrobnr98