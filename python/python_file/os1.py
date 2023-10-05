# 檔案和目錄
# import os
# print(os.getcwd())# getcwdc函式可以取得目前的工作目錄

# 刪除檔案
# remove函式:刪除檔案
# import os
# file = 'css.txt'
# if os.path.exists(file):# os.path的exists函式是檢查有沒有存在
#     os.remove(file)# 若有的話請刪除
# else:
#     print(file + "檔案未建立")# 若沒有的話，css.text檔案未建立

# mkdir檔案:
# import os
# Mymkdir = 'mymkdir'
# if not os.path.exists(Mymkdir):
#     os.mkdir(Mymkdir)# 顯示mymkdir資料夾
# else:
#     print(Mymkdir + "已經建立!")

# rmdir檔案:
# import os
# Mymkdir = 'mymkdir'
# if os.path.exists(Mymkdir):
#     os.rmdir(Mymkdir)
# else:
#     print(Mymkdir + "目錄未建立!")

# System函式:為了執行作業命令
# import os
# cur_path = os.getcwd() # 取得目前路徑
# os.system("cls")  # 清除螢幕
# os.system("mkdir dir2")  # 建立 dir2 目錄
# os.system("copy list.py dir2\copyfile.py") # 複製檔案
# file=cur_path + "\dir2\copyfile.py"
# os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔

# join函式:將叄數內字串結合成一個檔案路徑
# import os
#
# filename = os.path.abspath("os1.py")
# if os.path.exists(filename):
#     basename = os.path.basename(filename)
#     print("最後的檔案或路徑名稱：" + basename)
#
#     dirname = os.path.dirname(filename)
#     print("目前檔案目錄路徑：" + dirname)
#
#     print("是否為目錄：", os.path.isdir(filename))
#
#     fullpath, fname = os.path.split(filename)
#     print("目錄路徑：" + fullpath)
#     print("檔名：" + fname)
#
#     Drive, fpath = os.path.splitdrive(filename)
#     print("磁碟機：" + Drive)
#     print("路徑名稱：" + fpath)
#
#     fullpath = os.path.join(fullpath, fname)
#     print("組合路徑= " + fullpath)

# 實際操作
# import os
# cmd = os.getcwd()
# path = os.path.join(cmd)
# print(path+'image.png')

# os.walk函式:是可以搜尋指定目錄以及其子目錄。
# import os
# cur_path=os.path.dirname(__file__) # 取得目前路徑
# sample_tree=os.walk(cur_path)
# for dirname,subdir,files in sample_tree:
#     print("檔案路徑：",dirname)
#     print("目錄串列：" , subdir)
#     print("檔案串列：",files)
#     print()

# 實際操作:
# import os
# cur_path = os.getcwd()
# sample_tree = os.walk(cur_path)
# for dirname,subdir,files in sample_tree:
#     print("檔案路徑：",dirname)# 檔案路徑
#     print("目錄串列：" , subdir)# 目錄串列
#     print("檔案串列：",files)# 檔案串列
#     print()# 空一格

# shull模組:它是跨平臺的檔案處理模組，它提供一些函式，可以在python程式中執行檔案、刪除檔案、搬移檔案
# import os,shutil
# cur_path=os.path.dirname(__file__) # 取得目前路徑
# destfile= cur_path + "\\" + "new.py"
# shutil.copy("shutil.py",destfile )  # 檔案複製
# shutil.copyfile("shutil.py","D:\\new.py" )  # 檔案複製

# glob模組:可以指定條件的檔案串列
# import glob
# files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt")
# for file in files:
#     print(file)