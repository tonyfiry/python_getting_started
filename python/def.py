# 筆記8
# function(函式)

# def語法
# def helloword():
#     print("hello,word!!")
#     return "hello,word!!"
# helloword()

# 實際操作1:
# def total_money(a1,b1):
#     total = a1+b1
#     return total# 給它回傳值
# sum1 = total_money(100,10)# 輸入參數值
# print(sum1)

# 實際操作2:
# def ctor(c):
#     f = c * 1.8 + 32
#     return f
# inputc = float(input("請輸入攝氏溫度: "))
# print("華氏溫度為: %5.1f 度"%(ctor(inputc)))


# 函式變數有效範圍:
# 如何分辨區域變數跟全域變數
# def scope():
#     var1 = 1
#     print(var1,var2)# 1 20
#     # 這是區域變數
# var1 = 10
# var2 = 20
# scope()
# print(var1,var2)# 10 20
# # 全域變數

# global全域變數:
# def scope1():
#     global var1
#     var1 = 10
#     print(var1,var2)# 10 20
# var1 = 100
# var2 = 20
# scope1()
# print(var1, var2)# 10 20

# 數值函式整理
# abs(x):取得x的絕對值
# chr(x):取得整數x的字元
# divmod(x,y):取得x除以y的商及餘數的元組
# float(x):將x轉成浮點數
# hex(x): 將x轉換成十六進位數字
# int(x): 將x轉成整數
# len(x): 取得元素個數
# max(x): 取得參數串列中的最大值
# min(x): 取得參數串列中的最小值
# oct(x): 將x轉八進位數字
# ord(x): 回傳字元x的Unicode編碼值
# pow(x,y):取得x的y次方
# round(x):以四捨五入法取得x的近似值
# str(x):將x轉成字串
# sum(x):計算串列元素的總和

# pow(x,y)語法:
# p = pow(22,2)
# print(p)# 22的2次方是484
# p1 = pow(22,2,2)
# print(p1)# 餘數是0

# divmod()語法:
# d = divmod(22,2)
# print(d)#(11, 0)是元組形成的
# print(d[0],d[1])#d[0]是商數,d[1]是餘數,然後執行是11 0

# round()語法:
# r = round(24.2)
# print(r)#用四捨五入法是24
# r1 = round(r,4)# 可以設y是小數位數
# print(r1)# 一樣是24

# 實際操作:
# fraction1 = int(input("請輸入數字"))
# fraction2 = int(input("請輸入數字"))
# ret = divmod(fraction1,fraction2)
# print(f"這樣分數是{ret[0]},然後得到餘數是{ret[1]}")

# max()語法:
# g = [1,2,3,4,5]
# print(max(g))# 5

# min()語法:
# g = [1,2,3,4,5]
# print(min(g))# 1

# sum()語法:
# s = {1,2,3,4,5}
# s1 = list(s)# 轉成串列
# print(max(s1))# 5

# sorted()語法:
# g = []
# i = 0
# while i != -1:
#     i = int(input("請輸入數字"))
#     g.append(i)
# print(sorted(g))# [-1, 12, 22, 23]
# print(sorted(g,reverse=True)) # [23, 22, 12, -1]

# 字串函式
# center(n): 將字串擴充為n個字元且置中
# find(s):搜尋s字串在字串結尾
# endswith(s):字串是否以s字串字尾
# islower():字串是否都是小寫字母
# isupper():字串是否都是大寫字母
# s.join(list):將串列中元素以s字串作為連接字元組成一個字串
# len(字串):取得字串長度
# ljust(n):將擴充為n個字元且靠左
# lower():將字串字元都轉為小寫字母
# lstrip():移除字串左方的空白字元
# replace(s1,s2):將字串中的s1字串以s2字串取代
# rjust(n):將擴充為n個字元且靠右
# rstrip():移除字串右方的空白字元
# split(s):將字串以s字串為分隔字元分割為串列
# startswith(s):字串是否以s字串開頭
# strip():移除字串左右方的空白字元
# upper():將字串字元都轉為大寫字母

# #連接字串
# s.join()語法():
# list1 = ["鯨魚","獅子","老虎","狼"]
# s = ",".join(list1)
# print(s)# 鯨魚,獅子,老虎,狼

# while 迴圈實作
# list2 = []
# n = ""
# while n != "-1":
#     n = input("請輸入: ")
#     list2.append(n)
# print(list2)
# s = ",".join(list2)
# print(s)

# #分割字串
# split()語法:
# str1 = "what are you do?"
# split1 = str1.split(" ")
# print(split1)#['what', 'are', 'you', 'do?']
# print(split1.index('what'))# 0


# startswith()語法:
# str1 = "what are you do?"
# print(str1.startswith("w"))# True
# print(str1.startswith("o"))# False 不能用O來開頭，所以用w來開頭

# endswith()語法:
# str2 = "yes?"
# print(str2.endswith("?"))# True
# print(str2.endswith("y"))# False 不能用y來結尾，所以用?來結尾

# # 字串排版
# ljust()語法:
# s = "python"
# print(s.ljust(8,"a"))#pythonaa
#
# rjust()語法:
# s1 = "python"
# print(s1.rjust(8,"2"))# 22python
# print(s1.rjust(12))

# center()語法:
# print("笨蛋".center(4,"哈"))# 哈笨蛋哈

# for 迴圈實作:
# n = int(input("請輸入數字:"))
# for i in range(1,n+1):
#     print("笨蛋".center(4,"哈"))

# # lstrip()語法:
# name = "   python   "
# s1 = name.lstrip()# 移除字串右方的空白字元
# print(s1)# python

# rstrip()語法:
# name1 = "  book  "
# s1 = name1.rstrip()# 移除字串左方的空白字元
# print(s1)#  book

# 實際操作:
# schoolname = ["小明","小蘭","小綠","小綠"]
# math = [100,99,67,87]
# chinese = [45,55,87,21]
# english = [90,70,69,44]
# print("姓名  座號  數學成績  國文成績  英文成績")
# for i in range(0,4):
#     print(schoolname[i].ljust(3),str(i+1).rjust(2),
#           str(math[i]).rjust(7),str(chinese[i]).rjust(7),str(english[i]).rjust(7))

# #搜尋字串
# find()語法:
# w = "What are you doing?".find("W")
# print(w)# 0 意思是搜尋結果是零，因為是索引值關係，必須從0開始。

# 取代字串
# replace()語法:
string1 = "你閉嘴拉!"
print(string1.replace("閉嘴","很乖"))
