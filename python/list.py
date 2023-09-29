# 筆記 5
# list 串列進階
# list1 = [1,2,3,4,5]
# l = list1[1:4:2]
# for i in l:
#     print(i,end=" ")#2 4

# append將資料加入到後面，但可以加入元素。
# list2 = [30,44,55]
# list2.append([65,88])# 將加入65裡面
# print(list2)

# 實際操作:
# s = []
# total = list2 = 0
# while list2 != -1:
#     list2 = int(input("請輸入數字:"))
#     s.append(list2)
# print("累積{}".format(len(s)-1))
# for i in range(0,(len(s)-1)):
#     total += s[i]
# print("total：%d 分" % total)

# insert:將元素加在串列的指定位置，索引值若超過串列值，就會跑到後面。
# list2 = [111,222,333]
# list2.insert(123,444)
# print(list2)

# extend:將資料加入到後面，但不可以加入元素。
# list3 = ["小綠","小黃","小蘭"]
# list3.extend(["小呂"])
# print(list3)

# # pop:將串列取出元素，同時串列會將該元素移除。
# list4 = [1,2,3,4,5]
# list4.pop(3)
# list4[0] = 12
# print(list4)# [1, 2, 3, 5]
#
# for list5 in list4:
#     print(list5,end=" ")#12 2 3 5

# list 轉 dict
# list1 = ['年紀','身高']
# list2 = [11,165]
# d = dict(zip(list1,list2))
# print(d)

rows1 = {'姓名':'tony','身高':165,'體重':65}
rowslist1 = list(rows1)
print(rowslist1)