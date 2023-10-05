# # 筆記1
# # 整數(int)、浮點數(float)
# num1 = 34 #整數
# num2 = 67.83 #浮點數
# num3 = 34.0 #浮點數
#
# # 布林值(bool)
# flag1 = False ##布林值
# flag2 = True #布林值
#
# # 字串
# str1 = "這是字串"
# str2 = '小明說:"您好!"'
#
# # 特殊符號
# # 脫逸字元 : \
# # \' : 單引號 , \" : 雙引號
# # \\ : 反斜線 , \n : 換行
# # \r : 游標到列首 , \t : Tab 鍵
# # \v : 垂直定位 , \a : 響鈴
# # \b : 後退鍵(BacksSpace)
# # \f : 換頁 , \x : 以十六進位表示位元
# # \o : 以八進位表示位元
#
#
# # type:會取得項目查詢資料類型
# print(type(1234))
# print(type("你好喔!"))
# print(type(False))
# print(type(34.0))
#
# # print():能列印所有內容 , sep ="分隔符號" , end = "結束字元"
#
# # 參數格式化 : %
# # %d:整數 、 %s:字串 、 %f:浮點數
# # %(數字)d : 控制列印位置，例如:%5d,%-2s,%12f
# name = '張騏'
# print('大家好，我的名字是%s'%(name))

# # 參數格式化 : formate()
# name = '林小明'
# score = 84
# print('{} 的成績 為 {}'.format(name,score))

#參數格式化；f
# name = "tonyiry"
# possword = 1234
# print(f'你的帳號是{name},然後你的密碼是{possword}')

# print("姓名  國文  數學  英文")
# print("%2s  %3d  %3d  %3d"%("小白",45,33,90))
# print("%2s  %3d  %3d  %3d"%("小綠",55,76,67))
# print("%2s  %3d  %3d  %3d"%("小黑",67,88,25))