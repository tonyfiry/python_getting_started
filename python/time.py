# #時間模組
# ctime():以傳入的時間數值來取得時間字串;
# sleep()語法:程式暫停停止執行n秒
# localtime()語法:取得時間日期和時間資訊。
# time():取得目前時間的數值;
# import time as t
# print(t.sleep(1))# 暫停1秒鐘

# t1 = t.time()# 取得時間數值
# print(t1)# 時間數值是1692194764.1293414

# t2 = t.sleep(1)# 讓程式暫停1秒鐘
# print(t2)# 暫停1秒鐘了

# print(t.localtime(t.time()))# 取得時間數值

# 可以用物件或索引值來表示
# def time1():
#     t3 = t.localtime(t.time())# 取得時間的資訊(抓取時間數值)
#     year = t3.tm_year# 利用物件來獲得年
#     mon = t3[1]# 利用索引值來獲得月
#     mday = t3.tm_mday# 利用物件來獲得日
#     print(year,mon,mday)#2023,8
# time1()#用函式執行

# 示範操作
import time as t  # 載入時間單位

week = [" 一", " 二", " 三", " 四", " 五", " 六", " 日"]
t4 = t.localtime()
print("今天是星期" + week[t4.tm_wday])



