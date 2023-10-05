# 筆記10
# 正規表達式

# def isTaiwanPhone(str):
#     if len(str) != 11:       # 如果長度不是11
#         return False         # 傳回非手機號碼格式
#     #檢查11個字元是否符合手機號碼格式
#     for i in range(0, 11):
#         if i==4:
#             if str[4] != '-':        # 如果第5個字元不是'-'字元
#                 return False         # 傳回非手機號碼格式
#         else: # 如果前4個字或最後6個字出現非數字字元
#             if str[i].isdecimal() == False:
#                 return False     # 傳回非手機號碼格式
#     return True                  # 傳回是正確手機號碼格式
#
# print("0937-123456 是台灣手機號碼：", isTaiwanPhone('0937-123456'))
# print("02-12345678 是台灣手機號碼：", isTaiwanPhone('02-12345678'))

# metch()方法:傳回字串起頭開始指定字串中符合正規表達式的字串，並將結果存入到MathObject物件中，若無符合字元，將變成None;
# 例:
# import re # 必須建立正規表達式物件
# pat = re.compile(r'\d{4}-\d{6}')# 建立re.compile()的物件
# m = pat.match('0933-950550')
#
# print(m)# <re.Match object; span=(0, 11), match='0933-950550'>
# print(m.group())# 0933-950550 是傳回符合正規表達式的字串，若無符合字元，將變成None;
# print(m.start())# 0 傳回match的開始位置
# print(m.end())# 11 傳回match的結束位置
# print(m.span())# (0, 11) 傳回(開始位置,結束位置)的元件物件。

# search()方法:是傳回指定第一組符合正規表達式的字串，並將結果存入MathObject物件中，若無符合字元，將變成None;
# 例:
# import re
# pat = re.compile('[a-z]+')
# p = pat.search('3tem34')
# print(p)# <re.Match object; span=(1, 4), match='tem'>
# print(p.group())# tem
# print(p.start())# 1
# print(p.end())# 4
# print(p.span())# (1,4)

# findall()方法:是傳回指定所有符合正規表達式的字串，並將結果存入MathObject物件中，若無符合字元，將變成None;
# import re
# pat = re.compile(r'[0-9]')
# p = pat.findall('123ffffsa')
# print(p)# ['1', '2', '3']

# 也可以不用靠re.compile()來表示:
# import re
# pat = r'\d{4}-\d{6}'
# p = re.match(pat,'0933-950550')
# print(p)
# print(p.group())
# print(p.span())
# print(p.start())
# print(p.end())

# 實際操作:
# import re
# numStr = 'tel:04-12345678'
# pat = r'(\d{2})-(\d{8})'
#
# phone = re.search(pat,numStr)
#
# if not phone == None:
#     print(phone.group())
#     print(phone.group(0))
#     print(phone.group(1))
#     print(phone.group(2))


# import re
# numStr = 'tel:(04)12345678'
# pat = r'\((\d{2})\)(\d{8})'# 使用\(\)來表示
#
# phone = re.search(pat,numStr)
# if not phone == None:
#     print(phone.group(0))# (04)12345678
#     print(phone.group(1))# 04
#     print(phone.group(2))# 12345678

# import re
# phonelist = ['(04)12345678','(04)-12345678']
# pat = r'\((\d{2})\)-?(\d{8})'# ?是可以出現1次或0次
#
# for phone in phonelist:
#     phoneNum = re.search(pat,phone)
#     if not phoneNum == None:
#         print(phoneNum.group())
# 實際操作:
# import re
# list1 = ['1234-1234','12341234']
# pat = r'^123'
# for phone in list1:
#     phoneNum = re.search(pat,phone)
#     if not phoneNum == None:
#         print(phoneNum.group())

# 使用|字元搜尋:
# import re
# PhoneList = ['0412345678','(04)12345678','(04)12345678','(049)2987654','0937-998877']
# pat = r'\(\d{2,4}\)-?\d{6,8}|\(\d{4}\)-\d{6,8}'
# for phone in PhoneList:
#     phoneNum = re.search(pat,phone)
#     if not phoneNum == None:
#         print(phoneNum.group())

# 字元分類
# import re
# pat = r'[0-9+]+'
# massage = '你今年是18歲喔，很會用C++'
# p = re.findall(pat,massage)
# print(p)

# 使用*字元搜尋
# *:是設定待搜尋字元可以出現0次到無限多次，例如:[abc]*
# import re
# pat = re.compile(r'[abc]*')
# massage = 'abc掰掰'
# p = re.findall(pat,massage)
# print(p)

# 使用+字元搜尋
# +:是設定待搜尋字元可以出現0次到無限多次，例如:[abc]+
# import re
# pat = re.compile(r'[abc]+')
# massage = 'abc掰掰abc'
# p = re.findall(pat,massage)
# print(p)

# 忽略英文大小寫
# import re
# pat = r'PYTHON|JAVA'
# s = 'I like python and java'
# p = re.findall(pat,s,re.I)
# print(p)#['python', 'java'] 變小寫

# 實際操作:
# import re
# pat = r'HOTDOG'
# s = 'I like a eat hotdog!!'
# p = re.findall(pat,s,re.IGNORECASE)
# print(p)

# 字元分類中^字元
# import re
# pat = r'[^a-z. ]+'
# s = 'John was 18 year old'
# p = re.findall(pat,s)
# print(p)

# 正規表達式中的^和$字元

# import re
# pat = r'^\d+'
# s = '2020 is coming soon'
# m = re.findall(pat,s)
# print(m)# ['2020']
# m2 = re.findall(r'\w+$', s)
# print(m2)# ['soon']


# 正規表達式中的.和*字元
# import re
# pat = r'.o'
# s = 'Do your best!'
# m = re.findall(pat,s)
# print(m)# ['Do', 'yo']
# m2 = re.findall(r'.*o', s)
# print(m2)# ['Do yo']


# 換列字串的處理
# import re
# pat = r'.*'
# s = "Do your best,\nGo GO Go!"
# m = re.search(pat, s)
# print(m.group())#Do your best,
# m2 = re.search(r'.*',s,re.DOTALL)# re.DOTALL是字串不換行
# print(m2.group())#Do your best,\n Go GO Go!

# import re
# phonelist = ['0412345678','(04)-12345678','(04)12345678','(049)2987654','0937-99887']
# pat = r'''\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}'''
# for phone in phonelist:
#     PhoneNum = re.search(pat,phone,re.VERBOSE)# re.VERBOSE是正規表達式的加上註解
#     if not PhoneNum == None:
#         print(PhoneNum.group())

# 使用re.sub()取代字串
# import re
# pat = r'\d+'
# substr = '*'
# s = 'Password:1234,id:234'
# result = re.sub(pat,substr,s)
# print(result)

# 實際操作
# import re
# def math(m):
#     v = int(m.group())# 用group()方法
#     return str(v*2)
# result = re.sub('\d+',math,'1 2 3 4 5',3)
# print(result)
