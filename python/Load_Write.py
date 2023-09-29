## 數據資料的儲存與存取
# CSV編輯方式
# 可以用串列或是字典類型，將資料寫入csv檔案。
# csv寫入物件.wrirterow():寫入一維串列
# csv寫入物件.writerows():寫入二維串列
# import csv #匯入csv模組

# with open('test1.csv','w',encoding='UTF-8',newline='') as file:
#     # 建立 csv 檔案寫入物件
#     write = csv.writer(file)
#     # 寫入欄位名稱
#     write.writerow(['name','height','weight'])
#     # 寫入欄位資料
#     write.writerow(['tony',170,44])
#     write.writerow(['tonfg',145,65])  

#實作
# import csv 

# with open('test2,csv','w',encoding='UTF-8',newline='') as file:
#     write=csv.writer(file)
#     write.writerow(['姓名','身高','體重'])
#     write.writerow(['tony',167,67.5])
#     write.writerow(['fish',150,45.5])

#二維資料將入csv檔案
# import csv
# list = ['姓名','身高','體重'],['tona',147,64.5],['aish',140,45.5] 
# with open('test3.csv','w',encoding='UTF-8',newline='') as file:
#     write1=csv.writer(file)
#     write1.writerows(list)

#將字典資料寫入csv檔案
# import csv
# with open('test4.csv','w',encoding='UTF-8',newline='') as file:
#     #定義欄位
#     fieldnames = ['姓名','身高','體重']

#     write = csv.DictWriter(file,fieldnames=fieldnames)
#     #寫入欄位名稱
#     write.writeheader()
#     #寫入資料
#     write.writerow({'姓名':'tony','身高':170,'體重':65})
#     write.writerow({'姓名':'gira','身高':167,'體重':45})

#csv檔案讀取(串列型態)
# import csv# 匯入csv模組
# with open('test4.csv','r',encoding='UTF-8',newline='') as file:
#     # 將檔案讀取
#     row = csv.reader(file)
#     #利用迴圈讀取       
#     for rows in row:
#         print(rows)

#csv檔案讀取(字典型態)
# import csv# 匯入csv模組
# with open('./test/test4.csv','r',encoding='UTF-8',newline='') as file:
#     # 將檔案讀取
#     row = csv.DictReader(file)#
#     #利用迴圈讀取       
#     for rows in row:
#         print(rows['姓名'],rows['身高'],rows['體重'])

#EXCEL檔案新增及儲存
# import openpyxl
# workbook = openpyxl.Workbook()# 建立工作室簿
# sheet = workbook.worksheets[0]# 取得工作表
# # sheet['A1'] = 'hello'
# # sheet['B1'] = 'world'
# datalist1 = ['姓名','身高','體重']
# sheet.append(datalist1)
# rows1 = ['tony',165,65]
# sheet.append(rows1)
# rows2 = ['totz',167,78]
# sheet.append(rows2)
# workbook.save('test5.xlsx')

# EXCEL檔案讀取及編輯
# import openpyxl
# workbook = openpyxl.load_workbook("test5.xlsx")# 讀取工作簿
# sheet = workbook.worksheets[0]# 取得工作表(第一層)
# print(sheet['A3'],sheet['A3'].value)# 取得指定的儲存格
# #用迴圈取得總行、列數,cell方法
# for i in range(1,sheet.max_row+1):
#     for j in range(1,sheet.max_column+1):
#         print(sheet.cell(row=i,column=j).value,end=" ")
#     print()# 讀取儲存格
# sheet['A3'] = 'raize'# 更新儲存格
# workbook.save("test5.xlsx")

# jason讀取資料
# import json # 匯入json模組
# class_str='''
# {
#     "一年三班":[
#         {
#             "座號": 15,
#             "姓名": "torty",
#             "身高": 165,
#             "體重": 65.5
#         },
#         {
#             "座號": 11,
#             "姓名": "grzo",
#             "身高": 145,
#             "體重": 32.5
#         },
#         {
#             "座號": 18,
#             "姓名": "fixz",
#             "身高": 170,
#             "體重": 32.5
#         }
#     ]
# }
# '''
# datas = json.loads(class_str)
# print(type(datas))
# for data in datas['一年三班']:
#     print(data,data['姓名'])

# load讀取jason讀取資料
# import json# 匯入json模組
# # 讀取資料
# with open('class_str.json','r',encoding='utf-8') as f:
#     data = json.load(f)
#     for datas in data['一年四班']:
#         print(datas,datas['姓名'])

# dumps輸出jason讀取資料
# import json# 匯入json模組
# with open('class_str.json','r',encoding='utf-8') as f:
#     data = json.load(f)# 讀取資料
# print(data,type(data))
# # 利用ensure_ascii(設定叄數)=Flase是為了讓資料中的中文能顯示正常
# dumpdata = json.dumps(data,ensure_ascii=False)
# print(dumpdata,type(dumpdata))

# dump輸出jason讀取資料
# import json
# with open('class_str.json','r',encoding='utf-8') as f:
#     datas = json.load(f)
# with open('new_class_str.json','w',encoding='utf-8') as f:
#     json.dump(datas,f,ensure_ascii=False)

#xml資料的儲存與讀取
#匯入xml.etree.ElementTree模組
# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.ElementTree as ET

#xml資料的讀取
# fromstring物件屬性和方法:
# 1.tag:標籤名稱 2.attrib:屬性名稱及值，可能多個，型態為字典。 3.text:內容(值)。
# 1.get()方法:讀取指定屬性名稱的值 set()方法:設定指定屬性名稱的值。

# import xml.etree.ElementTree as ET
# xml = '''\
# <?xml version="1.0" encoding="utf-8"?>
# <note 名字='tony'>
#   <to>Tove</to>
#   <from>Jani</from>
#   <heading>Reminder</heading>
#   <body>Don't forget me this weekend!</body>
# </note>

# '''
# root = ET.fromstring(xml)
# print(root.tag)
# print(str(root.attrib))
# print(str(root.text))
# print(str(root.get('名字')))
# root.set('date','data1')

# 讀取xml檔案
# 可以用parse()方法讀取xml檔案
# import xml.etree.ElementTree as ET
# tree = ET.parse('test.xml')
# # print(tree,type(tree))
# root = tree.getroot()
# print("tree資料型別:",type(root))
# print("根目錄標籤:"+root.tag)
# print("根目錄屬性:"+str(root.attrib))
#  讀取指定標籤資料:第一種用find()方法、第二種用findall()方法、第三種用iter(標籤名稱 = 值)方法
# r1 = root.find('parson')
# print("身高:" + r1[0].text)# 165
# r2 = root.findall('parson')
# print("體重:" + r2[1][0].text)# 145
# parson = list(root.iter(tag='parson'))
# for parsons in parson:
#   print(f"tag:{parsons.tag} attrib:{parsons.attrib} text{parsons.text}")

# XML資料的編輯

import xml.etree.ElementTree as ET
#xml = '''\
#<parson 名字='togd'><身高>185</身高><體重>65</體重><興趣>足球</興趣></parson>
#'''
# 用自訂函式
# root = ET.fromstring(xml)# 從字串載入並解析 XML 資料
# person = ET.Element('note')# 建立標籤
# person.attrib = {'名字':"tony"}# 設定 note 標籤的屬性和資料
# # 建立 person 標籤，並新稱屬性和資料
# tall = ET.SubElement(person,"身高")
# tall.text = 165
# weight = ET.SubElement(person,"體重")
# weight.text = 65.5
# root.append(person)
# print(root[2].get('名字'))

# 資料的儲存
# xml='''\
# <?xml version="1.0"?>
# <data 名稱="e-happy">
#     <person 姓名="David">
#       <身高>183</身高>
# 		  <興趣>長跑</興趣>
#     </person>
#     <person 姓名="Chiou">
#       <身高>170</身高>
# 		  <興趣>籃球</興趣>
#     </person>
# </data>
# '''
# def pretty_xml(element, indent, newline, level=0):
#     if element:  # 判斷element是否有子元素    
#         if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
#             element.text = newline + indent * (level + 1)
#         else:
#             element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
#     temp = list(element)  # 將element轉成list
#     for subelement in temp:
#         if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最後一個元素，表示下一行是同級别元素的起始，缩排應一致
#             subelement.tail = newline + indent * (level + 1)
#         else:  # 如果是list的最後一個元素， 表示下一行是母元素的结束，缩排應該少一個   
#             subelement.tail = newline + indent * level
#         pretty_xml(subelement, indent, newline, level=level + 1)  # 對子元素進行遞迴操作

# root = ET.fromstring(xml)# 從字串載入並解析 XML 資料
# person = ET.Element('parson')# 建立標籤
# person.attrib = {'名字':"togd"}# 設定 note 標籤的屬性和資料
# # 建立 person 標籤，並新稱屬性和資料
# tall = ET.SubElement(person,"身高")
# tall.text = "185"
# weight = ET.SubElement(person,"興趣")
# weight.text = "足球"
# root.insert(1,person)
# print(root[1].get('名字'))

# pretty_xml(root,'\t','\n')# XML資料的縮排
# tree = ET.ElementTree(root)
# tree.write('new_test1.xml',encoding='utf-8')

#修改XML
import xml.etree.ElementTree as ET
xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
      <身高>183</身高>
		  <興趣>長跑</興趣>
    </person>
    <person 姓名="Chiou">
      <身高>170</身高>
		  <興趣>籃球</興趣>
    </person>
</data>
'''
root = ET.fromstring(xml)
root[0].set('姓名','鮭魚')
bobby = root[0].find('興趣')
bobby.text = '賽車'
# XML刪除資料
root.remove(root[0])
tree = ET.ElementTree(root)
tree.write('new_test2.xml',encoding='utf-8')


