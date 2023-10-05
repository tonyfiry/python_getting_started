# 例外處理(execption handling)
# try...except語法

# try:
#     print(few)# 顯示few
# except:
#     print("忘了用冒號!")#執行是忘了用冒號!

# try...except...else語法
# n = 2 # 變數是2
# try:
#     n+=1# 讓n+1進來
# except:
#     print("變數n不存在!")# 解釋是變數n不存在!
# else:
#     print("n =",n)# 最後執行到n = 3

# try..except Exception as e 語法:
# try:# 提出問題
#     n = ""
#     if n > 20:
#         print(n)
#     else:
#         print(n)
# except Exception as e:# 可以幫你捕捉錯誤訊息
#     print(e)

# 實際操作:
# n = 0
# try:
#     for i in range(1,10):
#         print(i,end=" ")
#
# except Exception as e:
#     print(e)

# try...except...finally
# try:
#     print(n)
# except:
#     print("變數n不存在!")
# finally:
#     print("一定會執行程式區塊")# 無論有沒有發生錯誤訊息，都會一樣照著執行。



