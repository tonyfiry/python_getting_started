# 筆記7
# 學會如何用集合(set)
# 集合(set)語法:
# set1 = {1,2,3,4,5,4}
# set2 = {"1","2","3","4","5"}
# print(set1)# {1, 2, 3, 4, 5},因為4不能重複，所以被蓋掉。
# print(set2)# {'2', '4', '1', '3', '5'}
# d1 = {}
# s1 = ()
# print(type(d1))# <class 'dict'>
# print(type(s1))# <class 'tuple'>

# 實際操作
# person = ["小名","小灰","小蘭"]
# s = set(person)
# print(s)
# list1 = list(s)
# print(list1)
# print(list1[0])

# 集合的操作
# &: 交集
# |: 聯集
# -: 差集
# ^: 對稱差集
# == : 等於
# != : 不等於
# in : 是成員
# not in: 不是成員

# &(交集)操作:
# A = {1,2,4,5}
# B = {3,4,6,7}
# print(A&B)# {4}

# |(聯集)操作:
# A = {1,2,4,5}
# B = {3,4,6,7}
# print(A|B)#{1, 2, 3, 4, 5, 6, 7}

# -(差集)操作:
# A = {1,2,4,5}
# B = {3,4,6,7}
# print(A-B)# {1,2,5}

# ^(對稱差集)操作:
# A = {1,2,4,5}
# B = {3,4,6,7}
# print(A^B)# {1, 2, 3, 5, 6, 7}

# add()用法:
# A = {1,2,4,5}
# B = {3,4,6,7}
# B1 = B.add(8)
# print(A|B)# {1, 2, 3, 4, 5, 6, 7, 8}

# clear()用法:
# A = {1,2,4,5}
# D = A.clear()
# print(D) # None，因為A清除掉了。

# copy()用法:
# A3 = {45,55,100}
# A4 =A3.copy()
# A4.add(101)
# print(A4)

# discard()用法:
# A4 ={100,1000,10000}
# A4.discard(100)
# print(A4)# {1000, 10000}
# print(A4.discard(6000))# None:因為不存在就不影響錯誤直接None。

# remove()用法:
# A4 = {100,1000,10000}
# A4.remove(100)
# print(A4)# {1000, 10000}
# print(A4.remove(1200))# 錯誤:因為不存在無法刪除。

# pop()用法:
# A5 = {100,200,300}
# A5.pop()
# print(A5)#{100,300}
# print(A5.pop())
# A5.clear()
# print(A5)# set()

# update()用法:
# A = {1,2,3,4,5}
# B = {"Python","C++","Java"}
# A.update(B)
# print(A)

#max()用法:
# R = {1,2,4,100}
# print(max(R))
# print(min(R))
# print(sum(R))

#len()用法:
# R = {1,2,4,100}
# print(len(R))

#sorted()用法:
# R1 = {1,2,3,4,5,100}
# s = sorted(R1)
# s2 = sorted(R1,reverse=True)
# print(s)# [1, 2, 3, 4, 5, 100]
# print(s2)# [100, 5, 4, 3, 2, 1]

# enumerated()用法:
# R2 = {1,2,3,4,5,100}
# s = enumerate(R2)# 轉換成 enumerate 物件
# s1 = list(s)# [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 100)]
# print(s1)
# for i in s1:
#     print(i)
# for i,item in s1:
#     print(i,item)

# frozenset:凍結集合
a = frozenset([1,2,4,5,6])
b = frozenset([7,8,9,10,11])

print(a&b)# frozenset()
print(a|b)# frozenset({1, 2, 4, 5, 6, 7, 8, 9, 10, 11})
print(a-b)# frozenset({1, 2, 4, 5, 6})
print(b-a)# frozenset({7, 8, 9, 10, 11})
print(a^b)# frozenset({1, 2, 4, 5, 6, 7, 8, 9, 10, 11})
print(max(a))# 6
print(min(a))# 1
print(max(b))# 11
print(min(b))# 7
print(sum(a))# 18
print(sum(b))# 45

