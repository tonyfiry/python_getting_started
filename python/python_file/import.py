# 筆記9
# import模組語法

# import (模組名稱)第一種方法;
# from (模組代號) import (模組名稱)第二種方法;
# import  (模組名稱) as (模組代號)第三種方法;

# # random隨機亂數(數字):
# import random as r# 利用random模組;
# print(r.randint(0,5))# 出現產生是1;
# print(r.randrange(0,10,2))## 出現產生是8，也是整數亂數;跟ranint()雷同
# print(r.random())# 0.7386433501353307，功能是浮點數亂數。
# print(r.uniform(0,5))# 2.1059199136492635，功能是浮點數亂數。跟random()雷同

# import random as r
# while True:
#     r1 = r.randint(0, 5)# 使用整數亂數
#     print("隨機數字是:"+str(r1))
#     break# 不讓它無窮迴圈。

# #隨機取得字元或是串列元素
# choice()語法:# 隨機取得一個字元或串列元素
import random as r
h = "python"
print(r.choice(h))# 會隨機字串或串列

# for迴圈:
for i in range(0,5):# 執行五次
    print(r.choice(["1", "2", "3"]),end=" ")#3 3 2 3 2 出現五次隨機亂數

# sample()語法: # 跟choice()雷同，只是隨機取得多個字元或串列元素
import random as r
# h = "python"
# print(random.sample(h,1)# 抓取一個字串亂數

list1 = ["小綠","小黃","小蘭"]
for i in range(0,1):# 執行1次
    print(r.sample(list1,1))# 抓取一個字串亂數









