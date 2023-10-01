# 繪製折線圖
# import matplotlib.pyplot as plt

# listx = [2,4,6,8,10,12]
# listy = [1,3,5,7,12,32]
# # linewidth or lw:設定線性寬度，預設值1.0。
# # linestyle or ls:設定線性樣式，設定'-'(實線),'--'(虛線),':'(點線)。
# # color:設定顏色。
# # marker:設定標記樣式。
# # marksize or ms:設定標記大小。
# # Label:設定圖例名稱。
# plot = plt.plot(listx,listy,color = "blue",lw ='1.5',ls='--',label="solid-1")# 繪製折線圖，還有其他設定。
# plt.legend()# 必須要搭配legend函數才能讓label顯示出來。

# 設定標題
# plt.title("test title",fontsize=19)
# plt.xlabel("x-label",fontsize=19)
# plt.ylabel("y-label",fontsize=19)
# plt.show()#顯示

# 設定座標範圍
# import matplotlib.pyplot as plt
# listx = [1,5,7,9,13,16]
# listy = [15,50,80,40,70,50]
# plt.plot(listx, listy, color="black", lw="2.0", ls="--", label="label")
# plt.title("title-1",fontsize = 18)
# plt.xlabel("X-Label") # x座標標題
# plt.ylabel("Y-Label") # y座標標題
# x_label=plt.xlim(0,20) # 設定x座標範圍
# y_label=plt.ylim(0,100) # 設定y座標範圍
# plt.legend()# 必須要搭配legend函數才能讓label顯示出來。

# # 設定格線
# # alpha:設定透明度
# plt.grid(color="black",linewidth='1',linestyle=":",alpha=0.5)
# plt.show()

# 同時繪製多組資料
# import matplotlib.pyplot as plt

# listx_1 = [1, 5, 9, 13, 17]
# listy_1 = [5, 30, 15, 35, 5]
# plt.title("Test_Title",fontsize=11)
# plt.plot(listx_1,listy_1,color="green",linestyle="--",label="label-1")
# plt.legend()
# listx_2 = [1, 5, 9, 13, 17]
# listy_2 = [1,23,14,19,14]
# plt.plot(listx_2,listy_2,color="blue",linestyle="--",label="label-2")
# plt.legend()
# plt.xlabel("X-label",fontsize=11)
# plt.ylabel("Y-label",fontsize=11)
# plt.show()

# 設定座標刻度
# import matplotlib.pyplot as plt

# listx_1 = [1,2,3,4,5]
# listy_1 = [5, 2, 4, 3, 5]
# plt.title("Test_Title",fontsize=11)
# plt.plot(listx_1,listy_1,"r--*",label="label-1")
# plt.xticks(listx_1)# 設定x的座標刻度
# plt.yticks(listy_1)# 設定y的座標刻度
# plt.tick_params(axis='both',color="red",labelsize='16')# 設定座標刻度格式
# plt.legend()
# listx_2 = [1,2,3,4,5]
# listy_2 = [1,3,2,1,5]
# plt.plot(listx_2,listy_2,"g--p",label="label-2")
# plt.xticks(listx_2)# 設定x的座標刻度
# plt.yticks(listy_2)# 設定y的座標刻度
# plt.tick_params(axis='both',color="red",labelsize='16')# 設定座標刻度格式
# plt.legend()
# plt.xlabel("X-label",fontsize=11)
# plt.ylabel("Y-label",fontsize=11)
# plt.show()

#實戰:學會繪製折線圖
# import matplotlib.pyplot as plt

# year = [2018,2019,2020,2021,2022,2023]
# list1 = [20,15,20,22,55,90]
# plt.plot(year,list1,'g--s',lw="1.5",ms="6",label="apple")
# list2 = [1,20,30,45,55,80]
# plt.plot(year,list2,'b--s',lw="1.5",ms="6",label="banana")
# plt.ylim(0,100)
# plt.xticks(year)
# plt.tick_params(axis='both',labelsize="10",color="black")
# plt.title("line chart",fontsize=18)
# plt.xlabel("x-label",fontsize=18)
# plt.ylabel("y-label",fontsize=18)
# plt.grid(color="grey",lw='1',ls='--',alpha=0.5)# 設定格線
# plt.show()


# matplotlib圖示改中文
# import matplotlib.pyplot as plt


# year = [2018,2019,2020,2021,2022,2023]
# list1 = [20,15,20,22,55,90]
# plt.plot(year,list1,'g--s',lw="1.5",ms="6",label="apple")
# list2 = [1,20,30,45,55,80]
# plt.plot(year,list2,'b--s',lw="1.5",ms="6",label="banana")
# plt.ylim(0,100)
# plt.xticks(year)
# plt.tick_params(axis='both',labelsize="10",color="black")
# plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
# plt.rcParams['axes.unicode_minus'] = False 
# plt.title("標題",fontsize=18)
# plt.xlabel("年數",fontsize=18)
# plt.ylabel("分數",fontsize=18)
# plt.grid(color="grey",lw='1',ls='--',alpha=0.5)# 設定格線
# plt.show()

import twstock
twstock.__update_codes()
