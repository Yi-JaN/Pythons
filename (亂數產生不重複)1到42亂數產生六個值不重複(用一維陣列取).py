import random #要用亂數,所以先設一個random
data=[] #用一維陣列取值
for i in range(0,6,1) : #用一維陣列取我6個值,陣列第一個值為0,所以從0開始,每循環1次+1
    data+=[random.randint(1,42)] #每循環到這裡就亂數產生1~42中1個值,然後推給data一維陣列
    for j in range(0,i,1) : #for j角色是針對目前i值前面的值做審查動作,看有沒有重複的數字
        if data[j]==data[i] : #如果目前的j值跟我目前的i值是一樣的話就進去,沒有就略過換下一個j值
            data[i]=random.randint(1,42) #進去之後就針對目前的i值做重新亂數產生1~42
            if data[j]==data[i] : #產生完,在檢查一次看有沒有重複                 
                data[i]=random.randint(1,42) #有就在一次針對目前的i值做重新亂數產生1~42
for k in range(0,6,1) : #等到上面for i以此類推OK之後,for k就負責列印data一維陣列上的值
    print(data[k],end="\t") #每循環一次就列印data目前位置值[k]上的值
print()  #列印完後換行

#補充:data[i]=random.randint(1,42) ->這裡可以直接針對目前i值做重新亂數的動作,因為之前data+=[random.randint(1,42)]這行是
#                                    因為該位置值上沒有值,所以才用推的給data,來到這邊位置值上已經有值了,所以可以直接針對
#                                    此i值做重新亂數1~42的動作!              