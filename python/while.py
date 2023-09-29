# 筆記 4
# 串列(list)

# list1 = ['香蕉']#簡易的串列語法
# print(list1)


# list2 = [1,2,3,4]# 元素為1,2,3,4
# list3 = ["香蕉","蘋果","梨子"]# 元素為 香蕉, 蘋果, 梨子
# print(list2,list3)#開始執行
# 注意索引值是從零開始，不然它會出錯。

# list4 = ["牛肉","豬肉","羊肉","雞肉"]
# print(list4[0])# 索引值是牛肉。
# print(list4[4])# 索引值出錯，因為找不到索引值。

#多維串列
# list5 = ["牛肉","豬肉","羊肉","雞肉"],["香蕉","蘋果","梨子"]
# print(list5)# 索引值所有都列印出來
# print(list5[0][2])# 羊肉

# 實際操作:
# name = ["小明","小黃","小蘭"]
# score1 = [69,88,45]
# print("學生的名字是{}".format(name[1]))
# print("學生的分數是{}".format(score1[1]))

# 實際操作2:
# name = ["小明","小黃","小蘭"]
# score = ["69","88","45"]
# name1 = input("請輸入名字: ")
# score1 = input("請輸入數字: ")
#
# if name1 == name[0] and score1 == score[0]:
#     print("學生的名字是{} ".format(name1))
#     print("學生的分數是{} ".format(score1))
# elif name1 == name[1] and score1 == score[1]:
#     print("學生的名字是{} ".format(name1))
#     print("學生的分數是{} ".format(score1))
# elif name1 == name[2] and score1 == score[2]:
#     print("學生的名字是{} ".format(name1))
#     print("學生的分數是{} ".format(score1))
# else:
#     print("很抱歉，沒有這個人喔")

# range函式:
# ListVariable = range(start,stop)

# r1 = range(1,10)
# print(r1)

# r2 = range(3,8)
# print(list(r2))# [3,4,5,6,7]
# r3 = range(-6,-2)
# print(list(r3))# [-6,-5,-4,-3,-2]

# ListVariable = range(start,stop,step)
# list3 = range(1,8,1)
# print(list(list3))# [1, 2, 3, 4, 5, 6, 7]
# list4 = range(1,8,2)
# print(list(list4))# [1, 3, 5, 7]


# for 迴圈:通常用於來固定次數的迴圈。

#for variable in range: *for的語法
    #程式區塊

# 操作1
# for i in range(0,10):
#     i = i+1
#     print(i,end = " ")#1 2 3 4 5 6 7 8 9 10

# 操作2
# n = int(input("請輸入數字: "))
# for i in range(0,n+1):
#     i = i+1
#     print(i,end = " ")#1 2 3 4 5 6 7 8 9 10

# n = int(input("請輸入數字: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum+i
# print(sum,end= " ")#55

# for i in range(1,n+1):
#     sum = sum+i
#     print(sum,end= " ")# 1 3 6 10 15 21 28 36 45 55

# list1 = [1,2,3,4,5]
# for i in list1:
#     print(f"{i}",end=" ")#1 2 3 4 5

# sum = 0
# n = 10
# for i1 in range(1,n+1):
#     sum += i1
# print("1 到 %d 總和是 %d "%(n,sum))

#for 巢狀迴圈
# for i in range(1,10):
#     for j in range(1,10):
#         print("%d*%d=%-2d"%(i,j,i*j),end=" ")
#     print()
# n = int(input("請輸入: "))
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print('*', end='')
# #     print()#繪製直角三角形


# break 語法
# n = 10
# for i in range(1,n+1):
#     if i == 6:# 判斷說i要到6
#         break# 直到6結束
#     print(i,end=" ")# 1 2 3 4 5

# continue 語法
# n = 10
# for i in range(1,n+1):
#     if i == 6:
#         continue
#     print(i,end=" ")# 1 2 3 4 5 7 8 9 10


# score = [123,44,55]
#
# for i in score:
#     i = int(input("請輸入數字: "))
#     if i == 123:
#         print("通關")
#         break
#     else:
#         print("不能通過")
#         break
# print("結果是 {}".format(i),end=" ")

# for...else語法
# n = int(input("請輸入整數:"))

# if n == 3:
#     print("是奇數!")
# else:
#     for i in range(2,n+1):
#         if n % i == 0:
#             print("是偶數阿")
#             break
#     else:
#         print("這些都不是偶數或奇數!")

#while迴圈: 通常用於沒有固定次數的迴圈。
# sum1 = 0
# n = int(input("請輸入數字: "))
# while n < 10:
#     n += 1
#     sum1 += n
# print("{}".format(sum1),end= " ")#列印結果是55

# n = 0
#
# while n < 10:
#     n += 1
#     print("{}".format(n),end= " ")

# n = 0
# # 測試偶數
# while n < 10:
#     n += 2
#     print("{}".format(n),end= " ")#2 4 6 8 10

n = 0
# # 測試奇數
# while n < 10:
#     n += 3
#     print("{}".format(n),end= " ")# 3 6 9 12

# 玩密碼遊戲
# n = 0
# while n != 3:
#     possword = int(input("請輸入密碼: "))
#     if possword != 1234:
#         print(f"不是{possword}，重打一遍")
#         n += 1
#     else:
#         print(f"是{possword}，恭喜你喔")
#         n += 1







