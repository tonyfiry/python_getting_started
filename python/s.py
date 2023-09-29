#Selenium:瀏覽器自動化操作
from selenium import webdriver

driver = webdriver.Firefox()#
url='https://zh-tw.facebook.com/'#連結網址
driver.get(url)#連結google網站
email = 'tbo79435@gmail.com'#我的帳號
password = '33@3M310c766'#我的密碼
driver.find_element_by_id('email').send.keys(email)#輸入郵件
driver.find_element_by_id('pass').send.keys(password)#輸入密碼
driver.find_element_by_name('tbo79435@gmail.com').click()#按登入鍵