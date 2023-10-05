# 筆記7
# 學會如何用字典(dict)

# 第一種寫法:
# dict1 = {"小蘭":50,"小綠":80,"小黃":99}
# print(dict1["小綠"])#80
# 第二種寫法:
# dict1 = dict([["小蘭",50],["小綠",80],["小黃",99]])
# print(dict1["小黃"])#99

# 當字典的鍵重複:
# dict2 = {"小蘭":50,"小綠":80,"小黃":99,"小蘭":100}
# print(dict2["小蘭"])#100,因為有重複，所以把前面覆蓋執行到後面。
# 當字典不存在時:
# dict3 = {"小蘭":50,"小綠":80,"小黃":99}
# print(dict3)# {'小蘭': 50, '小綠': 80, '小黃': 99}
# print(dict3[50])# 錯誤
# print(dict3["小黑"])# 錯誤

# 當字典不存在或是字典的鍵重複時，用get的語法:
# dict4 = {"小蘭":50,"小黑":80,"小黃":99}
# print(dict4.get("小黃"))# 99
# print(dict4.get("小黃",44))# 99
# print(dict4.get("小藍"))# None
# print(dict4.get("小藍",88))# 88

# 實際操作
# dict5 = {"A":"獅子","B":"獵豹","C":"老鷹","D":"老虎"}
# name = input("請輸入你喜歡的動物代號: ")
# n = dict5.get(name)
# if n == None:
#     print("可惜沒有這個動物!")
# else:
#     print('太好了，看來你喜歡{}喔!'.format(n))

# 修改字典:
# dict6 = {1:23,2:22,3:55}
# dict6[1] = 100
# print(dict6)# {1: 100, 2: 22, 3: 55}
# dict6[4] = 200
# print(dict6)# {1: 100, 2: 22, 3: 55, 4: 200}

# 刪除字典:
# dict6 = {1:23,2:22,3:55}
# del dict6[3]
# for i in dict6:
#     print(dict6[i],end=" ")# 23 22

# dict6 = {1:23,2:22,3:55}
# del dict6
# print(dict6)#已經不存在了

# 字典進階:
# d = dict([[1,22],[2,22],[3,33]])
# print(2 in d)# True

# d1 = {1:22,2:33,3:44}
# for i in d1:
#     print(d1[i],end=" ")#22 33 44

# 實際操作:
# d2 = {"小蘭":50,"小綠":80,"小黃":99}
# name = input("請輸入學生的名字: ")
# if name in d2:
#     print(name + "的成績為 " +str(d2[name]))
# else:
#     score = int(input("請輸入學生的成績 :"))
#     d2[name] = score
#     print("字典內容:" + str(d2))

# keys()及vaules()功能
# dict10 = dict([[1,"Lion"],[2,"Cat"],[3,"Dog"],[4,"eagle"]])
# listname = list(dict10.keys())
# print(listname)
# listvaule = list(dict10.values())
# print(listvaule)

# 實際操作:
# d = {1:"蘋果",2:"香蕉",3:"奇異果",4:"火龍果"}
# listdkeys = list(d.keys())
# listd1value = list(d.values())
# for i in range(len(listdkeys)):
#     print(f"{listdkeys[i]}是{listd1value[i]}",end=" ")

# items()用法:
# d1 = {1:"蘋果",2:"香蕉",3:"奇異果",4:"火龍果"}
# ditems = d1.items()# dict_items([(1, '蘋果'), (2, '香蕉'), (3, '奇異果'), (4, '火龍果')])
# # print(list(ditems))
# # 用for看看
# l = list(ditems)
# for i in range(len(l)):
#     print(l[i])

# 實際操作
# dict1 = {"可樂":25,"雪碧":24,"咖啡":80}
# menu = list(dict1.items())
# for m,k in menu:
#     print('你的餐點是' + m + "這樣就要" + str(k))

# setdefault語法:
# dict4 = {1:"tony",2:"goda",3:"sdea"}
# print(dict4.setdefault(1))# tony
# print(dict4.setdefault(1,"disa"))# tony，因為沒辦法改
# print(dict4.setdefault(4))# None,鍵不存在
# print(dict4.setdefault(3,"lisa"))# sdea，因為沒辦法改