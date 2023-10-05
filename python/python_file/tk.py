# 筆記15
# 圖形使用者介面(GUI)

# geometry:功能為設定主視窗的尺寸。
# title:功能為設定主視窗的標題。
# 記得最後要使用mainloop()方法，因為讓程式進入與使用者互動模式。

# import tkinter as tk
# win = tk.Tk()
# win.geometry("450x100")# 主視窗的尺寸。
# win.title("這是主視窗")# 視窗標題
# win.mainloop()# 執行畫面

# 實際操作
# import tkinter as tk
# win1 = tk.Tk()# 視窗標題
# win1.geometry("450x200")
# win1.title("hello world!!")
# win1.mainloop()

#標籤元件
# import tkinter as tk
# win1 = tk.Tk()# 視窗標題
# win1.title("這是主視窗")#
# Label = tk.Label(win1,text="你好喔",width=32,height=32,font=("新細明體,12"),fg="black",padx=100,pady=20)# 建立標籤文件
# Label.pack()# pack方式是將元件視為矩形物件顯示。
# win1.mainloop()

#按鈕元件
# def chick1():
#     textvar.set("按過了")# 設定元件文字內容
# import tkinter as tk
# win = tk.Tk()# 視窗標題
# win.title("按鈕測試!")
# win.geometry("20x30")
# textvar = tk.StringVar()
# button = tk.Button(win,textvariable=textvar,command=chick1)
# textvar.set("按鈕")# 設定元件文字內容
# button.pack()
# win.mainloop()

# 實際操作
# def chick2():
#     chick = 12
#     if chick == 18:
#         intvar.set("恭喜已經是成年人")
#     else:
#         intvar.set("繼續加油!")
#
# # import tkinter as tk
# #
# # win = tk.Tk()
# # win.title("按鈕測試!")
# # win.geometry("20x30")
# # intvar = tk.IntVar()
# # button1 = tk.Button(win,textvariable=intvar,command=chick2)
# # intvar.set("測試1")
# # button1.pack()# pack方式是將元件視為矩形物件顯示。
# # win.mainloop()

# 改變標籤及按鈕元件文字內容
# def clickme():
#     global count
#     count += 1
#     labeltext.set("你按我 " + str(count) + " 次了！")
#     if(btntext.get() == "按我！"):
#         btntext.set("回復原來文字！")
#     else:
#         btntext.set("按我！")
#
# import tkinter as tk
#
# win = tk.Tk()
# labeltext = tk.StringVar()
# btntext = tk.StringVar()
# count = 0
# label1 = tk.Label(win, fg="red", textvariable=labeltext)
# labeltext.set("歡迎光臨Tkinter！")
# label1.pack()
# button1 = tk.Button(win, textvariable=btntext, command=clickme)
# btntext.set("按我！")
# button1.pack()
# win.mainloop()

# 實際操作
# def chick3():
#     labeltext.set('請按我吧!')
#     burtttext.set("恭喜發財!!")
#
# import tkinter as tk
#
# win = tk.Tk()
# win.title("按鈕測試!")
# labeltext = tk.StringVar()
# burtttext = tk.StringVar()
# Label = tk.Label(win,text="請開始按鈕!",fg="black",textvariable=labeltext)
# labeltext.set("測試1")
# Label.pack()
# button = tk.Button(win,text="請開始按鈕!",textvariable=burtttext,command=chick3)
# burtttext.set("開始按了")
# button.pack()
# tk.mainloop()

# 文字區域(Text)
# 元件名稱 = tk.Text(容器名稱,叄數1,叄數2)
# 例子:
# import tkinter as tk
#
# win = tk.Tk()
# win.title("文字測試")
# text = tk.Text(win,font=('標楷體',12),padx=10,pady=10)# 建立文字元件
# text.insert(tk.INSERT,"你好喔\n")# 加入文字
# text.insert(tk.END,"結束")
# text.pack()
# text.config(state=tk.DISABLED)
# win.mainloop()

# 實際操作:
# import tkinter as tk
# win = tk.Tk()
# win.title("Hello world!")
# text = tk.Text(win,font=("新細明體",12),fg="red")
# text.insert(tk.INSERT,"Hello world!\n")
# text.insert(tk.END,"End~~~")
# text.config(state=tk.DISABLED)
# text.pack()
# win.mainloop()

# 選項按鈕(RadioButton)及核選按鈕(CheckButton)
# 選項按鈕(RadioButton)元件:
# def choose():
#     msg.set("你喜歡運動是:"+choice.get())
# import tkinter as tk
# win = tk.Tk()
# win.title("文字測試")
# label = tk.StringVar()
# choice = tk.StringVar()
# msg = tk.StringVar()
# Label = tk.Label(win,text="選擇你喜歡運動是:")
# Label.pack()
# item1 = tk.Radiobutton(win,text="足球",value="足球",variable=choice,command=choose)
# item1.pack()
# item2 = tk.Radiobutton(win,text="籃球",value="籃球",variable=choice,command=choose)
# item2.pack()
# item3 = tk.Radiobutton(win,text="羽毛球",value="羽毛球",variable=choice,command=choose)
# item3.pack()
# lbmsg = tk.Label(win,fg="red",textvariable=msg)
# lbmsg.pack()
# item1.select()
# choose()
# win.mainloop()

#實際操作
# def Choose():
#     msg.set("你選擇喜歡的動物是:"+choice.get())#把這些選項變成單選


# import tkinter as tk#匯入tkinter套件

# win = tk.Tk()#主視窗畫面
# win.title("測試")#視窗標題
# Label = tk.Label(win,text="你最喜歡的動物是:",font=("新細明體",12),fg="red")#建立標籤
# Label.pack()#並矩形顯示
# choice = tk.StringVar()#建立字串變數
# msg = tk.StringVar()#建立字串變數
# item1 = tk.Radiobutton(win,text="cat",value="cat",variable = choice,command = Choose)#建立選項按鈕
# item1.pack()#並矩形顯示
# item2 = tk.Radiobutton(win,text="eagle",value="eagle",variable = choice,command = Choose)#建立選項按鈕
# item2.pack()#並矩形顯示
# item3 = tk.Radiobutton(win,text="fox",value="fox",variable = choice,command = Choose)#建立選項按鈕
# item3.pack()#並矩形顯示
# item1.select()#並選擇item1
# lbmsg = tk.Label(win,fg="red",textvariable=msg)#建立標籤
# lbmsg.pack()#並矩形顯示
# Choose()#呼叫Choose()
# win.mainloop()#啟動

#核選按鈕(checkbutton)元件
#元件名稱 = tk.checkbutton()
# def choose():
#     str = "你喜歡運動是: "
#     for i in range(0,len(choice)):
#         if choice[i].get() == 1:
#             str = str + ball[i] + " "
#     msg.set(str)

# import tkinter as tk

# win = tk.Tk()
# win.title("測試")
# choice = []
# ball = ["足球", "籃球", "棒球"]
# msg = tk.StringVar()
# label = tk.Label(win, text="選擇喜歡的球類運動：")
# label.pack()
# for i in range(0,len(ball)):
#     tem = tk.IntVar()
#     choice.append(tem)
#     item = tk.Checkbutton(win, text=ball[i], variable=choice[i], command=choose)
#     item.pack()
# lblmsg = tk.Label(win, fg="red", textvariable=msg)
# lblmsg.pack()
# win.mainloop()


#實際操作
# def choose():
#     str = "你選擇喜歡動物是: "
#     for i in range(0,len(choice)):
#         if choice[i].get() == 1:
#             str = str + anmal[i] + " "
#     msg.set(str)

# import tkinter as tk

# win = tk.Tk()
# win.title("測試!!")
# win.geometry("400x300")
# Label = tk.Label(text="你喜歡動物是: ",fg="yellow",bg="black",font=("粗體",12))
# Label.pack()
# msg = tk.StringVar()
# choice = []
# anmal = ["老鷹","獅子","老虎"]
# for i in range(0,len(anmal)):
#     tem = tk.IntVar()
#     choice.append(tem)
#     item = tk.Checkbutton(win,text=anmal[i],variable=choice[i],command=choose)
#     item.pack()
# lbmsg = tk.Label(font=("粗體",12),fg="blue",textvariable=msg)
# lbmsg.pack()
# win.mainloop()

#pack方法:為最基礎的佈局方式
# def text1():
#     msg.set("恭喜你選一")

# def text2():
#     msg.set("恭喜你選二")

# def text3():
#     msg.set("恭喜你選三")

# import tkinter as tk
# win = tk.Tk()
# win.title("測試!!")
# win.geometry("200x150")
# msg = tk.StringVar()
# Label = tk.Label(win,text="選吧",fg="red")
# Label.pack()
# button1 = tk.Button(win,text="button1",fg="blue",font=("新細明體",12),textvariable=text1,command=text1)
# button1.pack(padx=20,pady=5,side="top")#加入間距及位置
# button2 = tk.Button(win,text="button2",fg="blue",font=("新細明體",12),textvariable=text1,command=text2)
# button2.pack(padx=20,pady=5,side="left")#加入間距及位置
# button2 = tk.Button(win,text="button3",fg="blue",font=("新細明體",12),textvariable=text1,command=text3)
# button2.pack(padx=20,pady=5,side="right")#加入間距及位置
# lbmsg = tk.Label(win,fg="red",textvariable=msg)
# lbmsg.pack()
# win.mainloop()


#grid方法:表格式的排列方法。
# import tkinter as tk
# win = tk.Tk()
# win.geometry("300x200")
# button1 = tk.Button(text="box1",fg="green",font=("斜體",12))
# button1.grid(padx=20,pady=20,column=0,row=0)#控制row(列)以及column(行)
# button2 = tk.Button(text="box2",fg="green",font=("斜體",12))
# button2.grid(padx=20,pady=20,column=1,row=0)#控制row(列)以及column(行)
# button3 = tk.Button(text="box3",fg="green",font=("斜體",12))
# button3.grid(padx=20,pady=20,column=0,row=1)#控制row(列)以及column(行)
# button4 = tk.Button(text="box4",fg="green",font=("斜體",12))
# button4.grid(padx=20,pady=20,column=1,row=1,columnspan=22,rowspan=3)#控制row(列)以及column(行)
# win.mainloop()

#place方法:可以使用絕對位置來進行佈局。
# import tkinter as tk
# win = tk.Tk()
# win.geometry("300x100")#視窗寬度跟長度
# label1=tk.Label(win, text="輸入成績：")#建立標籤元件
# label1.place(x=20, y=20)
# score = tk.StringVar()
# entryUrl = tk.Entry(win, textvariable=score)#建立文字編輯元件
# entryUrl.place(x=90, y=20)
# btnDown = tk.Button(win, text="計算成績")
# btnDown.place(x=80, y=50)
# win.mainloop()

#實際操作
# def judge():
#     if score.get() == "1234":
#         msg.set("恭喜")
#     else:
#         msg.set("重考一遍吧")

# import tkinter as tk
# win = tk.Tk()
# win.geometry("300x100")#視窗寬度跟長度
# label1=tk.Label(win, text="輸入成績：")#建立標籤元件
# label1.place(x=20, y=20)
# score = tk.StringVar()
# msg = tk.StringVar()
# entryUrl = tk.Entry(win, textvariable=score)#建立文字編輯元件
# entryUrl.place(x=90, y=20)
# btnDown1 = tk.Button(win, text="計算成績",command=judge)
# btnDown1.place(x=80, y=50)
# Lbmsg = tk.Label(win,textvariable=msg)
# Lbmsg.pack(side="bottom")
# win.mainloop()

#視窗區塊(Frame)
# import tkinter as tk
# win = tk.Tk()
# frame1 = tk.Frame(win)#建立視窗區塊
# frame1.pack()#建立排版
# Label1 = tk.Label(frame1,text = "標籤一",fg = "black")
# entry1 = tk.Entry(frame1,fg = "black")#tk.DISABLED可編輯的意思。
# Label1.grid(row = 0 , column=0)
# entry1.grid(row = 0 , column=1)
# frame2 = tk.Frame(win)#建立視窗區塊
# frame2.pack()#建立排版
# button1 = tk.Button(frame2,text = "確定",fg = "black")
# button2 = tk.Button(frame2,text = "取消",fg = "black")
# button1.grid(row = 0 , column=0)
# button2.grid(row = 0 , column=1)
# win.mainloop()