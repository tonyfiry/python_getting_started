#數據資料的爬取
# import requests #匯入requests模組
# url = 'https://www.youtube.com/'
# r = requests.get(url)
# # 檢查HTTP回應碼是否為200(requests.code.ok)
# if r.status_code == requests.codes.ok:
#      print(r.text)

#發送Get請求:
# import requests as r  #匯入requests模組
# url = 'http://httpbin.org/get'#抓取網址
# request = r.get(url)#Get請求
# print(request.text)#列出網頁原始碼

#加上URL查詢叄數
# import requests as r #匯入requests模組
# payload = {'key1':'value1','key2':'value2'}#將查詢叄數放在Get裡面
# url = 'http://httpbin.org/get'
# r1 = r.get(url,params=payload)
# print(r1.text)

#發送POST請求:
# import requests as r#匯入requests模組
# url = 'http://httpbin.org/post'#將查詢叄數放在POST裡面
# payload = {'key1':'value1','key2':'value2'}
# r1 = r.post(url,data=payload)
# print(r1.text)#列出網頁原始碼

#自訂HTTP Headers 偽裝瀏覽器:
# import requests as r
# url = 'https://www.instagram.com/'#抓取網址
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
#     'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3'}
# #自訂標頭
# r1 = r.get(url,headers=headers)
# print(r1)#Response [200]

#使用Session 及 Cookie 進入認證頁面
# import requests as r
# url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# #設定cookie的值
# cookies = {'over18':'1'}
# r = r.get(url,cookies=cookies)
# print(r.text)

#實際操作
# import requests as r #匯入requests模組
# #設定url
# url = 'https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&service=accountsettings&ifkv=AYZoVhcdR5JLvwuTwnnW11SSNhtB7g9aQjYU5yWrXoA4CA4u1-jMB3OnZhyyTDIfepSq4eZkZhYP&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
# #設定cookie的值
# cookies = {'__Host-GAPS	':'1:8ZiF34c4hy5elrQOKOqOntllJd9tKnr3rCRFDS99UJJWSvo9Sl6G3_t0Xg1YwKFmslaPBOdylX-lzxp1clbbL2gR4dAh8g:RPlPKUEfJS0KG4mk'}
# r = r.get(url,cookies=cookies)
# print(r.text)#執行網路原始碼

#實戰:IP位址查詢
# import requests as r #匯入requests模組
# #設定url
# url = 'https://api.ipify.org/'
# r = r.get(url)#用get請求
# print("我目前的IP是",r.text)#執行結果是我目前的IP是 111.83.68.88

#BeautifulSoup模組(網頁解析模組)
#HTML的表示法是DOM(Document Object Model)(文件物件模型)
# from bs4 import BeautifulSoup#匯入BeautifulSoup模組
# import requests as r#匯入requests模組
# url = 'https://www.ptt.cc/bbs/Gossiping/M.1694276111.A.C4F.html'
# html = r.get(url)
# sp = BeautifulSoup(html.text,'html.parser')
# print(sp.text)
# print(sp.text.title)
# print(sp.h1)
# print(sp.p)


# find()使用方法:
# find():是尋找第一個符合條件的標籤，以字串回傳。
# from bs4 import BeautifulSoup #匯入BeautifulSoup模組
# def MyBeautifulSoup():#建立函式
#     #寫入HTML
#     html = '''
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>Page Title</title>
#         </head>
#         <body>
#             <h1>This is a Heading</h1>
#             <p>This is a paragraph.</p>
#         </body>
#         </html> 
#         '''
#     sp = BeautifulSoup(html,'html.parser')#BeautifulSoup基本用法
#     find1 = sp.find("h1")# <h1>This is a Heading</h1>
#     find2 = sp.find("title")# <title>Page Title</title>
#     #find_all():是尋找全部符合條件的標籤，以串列回傳。
#     find3 = sp.find_all("title")#[<title>Page Title</title>]
#     print(find1,find2,find3)
# MyBeautifulSoup()

#加入標籤屬性搜尋條件
# from bs4 import BeautifulSoup
# html = '''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Page Title</title>
#         <style>
#             .box-1{
#                 width:30px;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>This is a Heading</h1>
#         <h2 id=box-1>你好</h2>
#     </body>
#     </html> 
#     '''
# sp = BeautifulSoup(html,'html.parser')
# find1 = sp.find("h1")#<h1>This is a Heading</h1>
# find2 = sp.find('h2',{'id':'h2','id':'box-1'})#<h2 id="box-1">你好</h2>
# print(find1,find2)

#利用CSS選擇器找尋內容:select()
#select()方法:是用以CSS選擇器找尋內容,以串列回傳。
# from bs4 import BeautifulSoup
# html = '''
# <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Page Title</title>
#         <style>
#             .box-1{
#                 width:30px;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>This is a Heading</h1>
#         <h2 id=box-1>你好</h2>
#     </body>
#     </html> 
# '''
# sp = BeautifulSoup(html,'html.parser')#利用BeautifulSoup模組網頁解析
# css1 = sp.select('#box-1')#用select()方法找尋id，以串列回傳表示，
# print(css1)#[<h2 id="box-1">你好</h2>]

#取得標籤的屬性內容
# from bs4 import BeautifulSoup
# html = '''
# <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Page Title</title>
#         <style>
#             .box-1{
#                 width:30px;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>This is a Heading</h1>
#         <h2 id=box-1>你好</h2>
#         <a href="https://www.youtube.com/@JasonDerulo/videos">超連結</a>
#     </body>
#     </html> 
# '''
# sp = BeautifulSoup(html,'html.parser')#利用BeautifulSoup模組網頁解析
# css2 = sp.select('a')[0].get('href')#用select()方法找尋<a>標籤內容,用字典資料取值的方法取得，以串列回傳表示，
# print(css2)#[<h2 id="box-1">你好</h2>]

#實戰:
import requests
from bs4 import BeautifulSoup
url = 'https://www.pilio.idv.tw/ltobig/list.asp'
r = requests.get(url)
r.encoding = r.apparent_encoding
sp = BeautifulSoup(r.text,'html.parser')
title = sp.find('title').text
print("標題: ",title)



