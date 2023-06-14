#查詢三個考生的成績排序排名
data=[] #三個考生成績用一維陣列取起來
for i in range(0,3,1) : #陣列第一個值必為0,從0開始循環 0<3 每次循環+1
    data+=[int(input())] #每循環到這行就取一個自己輸入的值轉成int後再推給data
print("考生1的成績:",data[0]) #列印3位考生考出來的成績
print("考生2的成績:",data[1])
print("考生3的成績:",data[2])
if data[0]>data[1] and data[0]>data[2] and data[1]>data[2] : #排名判斷,如果是考生1最大的話,他的排名情況
  print("考生1>考生2>考生3")
elif data[0]>data[1] and data[0]>data[2] and data[2]>data[1] :
  print("考生1>考生3>考生2")
elif data[0]>data[1] and data[0]>data[2] and data[1]==data[2] and data[2]==data[1] :
  print("考生1>考生2==考生3")
elif data[1]>data[0] and data[1]>data[2] and data[0]>data[2] : #如果是考生2最大的話,他的排名情況
  print("考生2>考生1>考生3")
elif data[1]>data[0] and data[1]>data[2] and data[2]>data[0] :
  print("考生2>考生3>考生1")
elif data[1]>data[0] and data[1]>data[2] and data[0]==data[2] and data[2]==data[0] :
  print("考生2>考生1==考生3")
elif data[2]>data[0] and data[2]>data[1] and data[0]>data[1] : #如果是考生3最大的話,他的排名情況
  print("考生3>考生1>考生2")
elif data[2]>data[0] and data[2]>data[1] and data[1]>data[0] :
  print("考生3>考生2>考生1")
elif data[2]>data[0] and data[2]>data[1] and data[0]==data[1] and data[1]==data[0] :
  print("考生3>考生1==考生2")
else : #如果來到else這邊代表沒有排名結果,除非是3個值都一樣,才會來到這邊
  print("沒有排名結果")

#輸入->88 68 72                79 100 66                 70 70 70
#輸出->考生1的成績:88           考生1的成績:79            考生1的成績:70
#      考生2的成績:68           考生2的成績:100           考生2的成績:70
#      考生3的成績:72           考生3的成績:66            考生3的成績:70
#     考生1>考生3>考生2         考生2>考生1>考生3         沒有排名結果

#輸入->72 72 90
#輸出->考生1的成績:72
#      考生2的成績:72
#      考生3的成績:90
#     考生3>考生1==考生2