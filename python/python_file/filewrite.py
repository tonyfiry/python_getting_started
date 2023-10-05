# 檔案的讀寫
# (第一種方式)
# open函式
# text = """
# 不用寫這麼多了，哈哈哈
# welcome
# """
# f = open("file.txt", 'w',encoding="utf-8")
# f.write(text)
# f.close()
#
#
# f = open("file.txt", 'r',encoding="utf-8")
# for line in f:
#     print(line,end="")
# f.close()

# 實際操作:
# import os
# os.system('add file1.txt')
# text = """不用寫這麼多了，哈哈哈 welcome"""
# f = open("file1.txt", 'w',encoding="utf-8")
# f.write(text)
# f.close()
# f1 = open("file.txt", 'r',encoding="utf-8")
# for line in f1:
#     print(line,end="")
# f.close()

# (第二種方式)
# with open('file1.txt','r',encoding="UTF-8") as f:
#     for i in f:
#         print(i,end="")

# read
# text = """what are you name and age?"""
#
# with open('file.txt','w',encoding="UTF-8") as f:
#     write = f.write(text)
#     print(write)
#
# with open('file.txt','r',encoding="UTF-8") as f:
#     read = f.read()
#     print(read)# what are you name and age?

# readline:讀取目前的文字指標所在列中size長度的文字內容,若叄數省略，會讀取一整列，包括'\n'字元。
#  with open('file.txt','r',encoding="UTF-8") as f:
#      read = f.readline(5)
#      print(read)# what
#
# for i in range(len(read)):
#     i += 1
#     print(i, end=" ")

# readlines: 讀取全部文件內容，他會以串列方式傳回，每一列會成為串列中的一個元素。

# with open('file.txt','r',encoding="UTF-8") as f:
#     read = f.readlines()
#     print(read)#

# 二進位檔案的讀寫
# content='''Hello Python
# 中文字測試
# Welcome
# '''
#
# content=content.encode("utf-8") #轉成 bytes
# with open('file.bin','wb') as f:
#     f.write(content)
#
# with open('file.bin','rb') as f:
#     content=f.read().decode("utf-8")# 必須編碼是utf-8
#     print(content)

# seek():將指標到文件指定的位置，請注意:檔案必須以二進位模式開啟。
# tell():傳回文件目前的索引位置。

# file.bin 內容
# '''Hello Python
# 中文字測試
# Welcome
# '''
#
# f=open('file.bin','rb')
# print("目前文件索引位置：",f.tell()) #0
# f.seek(6) #移到索引第 6 (第7個字元)位置
# str1=f.read(7) #讀取 7 個字元
# print(str1)    # b'Python\n'
# print("目前文件索引位置：",f.tell()) #13
#
# f.seek(0) #回文件最前端
# print("目前文件索引位置：",f.tell()) #0
# str2=f.read(5) #讀取 5 個字元
# print(str2)    # b'Hello'
#
# f.seek(-8,2)   #移至最尾端，向前取 8 個字元
# str3=f.read()
# print(str3)    # b'Welcome\n'
#
# f.close()



