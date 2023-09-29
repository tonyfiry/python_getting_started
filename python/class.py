# 筆記9
# class Animal():# 定義類別
#     h = "hello world!!"# 定義屬性(attribute)
#     def sing(self):# 定義方法(method)
#         print("很會講喔")# 建立物件
#
# bird = Animal()# 建立叫 bird 的 Animal()! 物件
# print(bird.h)# hello world!!
# bird.sing()# 很會講喔

# 實際操作
# class addition():
#     a = int(input("請輸入數字: "))
#     b = int(input("請輸入數字: "))
#     def ab(self):
#         print("厲害答案是{}".format(addition().a+addition().b))
#
# a1 = addition().a
# a2 = addition().b
# print(a1+a2)
# addition().ab()

# 類別的建構式:
# def __init__(self[..叄數1,叄數2....])

# class Animal():# 定義類別
#     def __init__(self,name):
#         self.name = name #定義屬性
#     def sing(self):
#         print("很會唱歌")#定義物件
#
# bird = Animal("老師")# 用以 Animal() 物件 ，建立一個叫鸚鵡的 bird 物件
# print(bird.name)
# bird.sing()

# 實際操作
# class score1():
#     def __init__(self, score):
#         self.score = int(input("請輸入數字: "))
#     def ab(self):
#         if self.score == 100:
#             print("太棒了!")
#         elif self.score >= 90:
#             print("讚喔，考得很棒喔!")
#         elif self.score >= 80:
#             print("考得不錯!")
#         elif self.score >= 70:
#             print("考得還可以拉!")
#         elif self.score >= 60:
#             print("加油!繼續努力!")
#         else:
#             print("加油!你一定可以的")
# add1 = score1("")
# print(add1.score)
# add1.ab()

# 實踐操作2:
# class Aclass():# 建立類別
#     def __init__(self,name,age):#建立物件建構式
#         self.name = name# 建立屬性
#         self.age = age # 建立屬性
#     def sing(self):# 建立方法
#         print(f"{self.name}很會唱歌，但年紀是{self.age}")
#     def grow(self,year):# 建立方法
#         self.age += year
#
# bird = Aclass("鸚鵡",1)# 將創一個 鸚鵡 跟 1 的 Aclass()物件
# bird.grow(1)# 將年紀增加1歲
# bird.sing()# 鸚鵡很會唱歌，但年紀是2

# 類別封裝:
# class math():# 建立物件
#     def __init__(self,math):# 建立建構式
#         self.math = math # 建立共用屬性(attribute)
#     def __sing(self):# 建立私用方法
#         print("不就好棒棒，"+ self.math)
#     def grow(self):# 建立共用方法
#         self.__sing()
#
# m = math("555")
# print(m.math)
# m.grow()

# 類別繼承:
# 父類別(parent class)跟子類別(child class)

# class Animal():  # 定義父類別
#     def __init__(self, name):
#         self.name = name  # 定義共用屬性
#
#     def fly(self):  # 定義共用方法
#         print(self.name + "很會飛!")
#
# class Bird(Animal):  # 定義子類別
#     def __init__(self, name):
#         self.name = "粉紅色" + name  # 覆寫父類別的建構式
#
#     def sing(self):  # 定義子類別的方法
#         print(self.name + "也愛唱歌!")
#
# pigeon = Animal("小白鴿")  # 以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
# pigeon.fly()  # 小白鴿很會飛!
#
# parrot = Bird("小鸚鵡")  # 以 Bird 類別，建立一個名叫小鸚鵡的 parrot 物件
# parrot.fly()  # 粉紅色小鸚鵡很會飛!
# parrot.sing()  # 粉紅色小鸚鵡也愛唱歌!

# 實際操作:
# class message1():
#     def __init__(self,name):
#         self.name = name
#     def call(self):
#         print(self.name +"很會叫!\n")
#
# class message2(message1):
#     def __init__(self,name):
#         self.name = name
#     def fly(self):
#         print(self.name + "很會飛!")
#     def sing(self):
#         print(self.name + "很會耍帥!")
#
# dog = message1("狗")
# print("原來是{}".format(dog.name))
# dog.call()
#
# eagle = message2("老鷹")
# print("原來是{}".format(eagle.name))
# eagle.fly()
# eagle.sing()
# eagle.call()

# 類別多型:
# class message1():
#     def __init__(self,name):
#         self.name = name
#     def call(self):
#         print(self.name +"很會叫!")
# class message2(message1):
#     def __init__(self,name,age):
#         self.__age = age
#         super().__init__(name)# 使用父類別的屬性
#     def year(self):
#         print("是" + str(self.__age) + "歲")
# class message3():
#     def sing(self):
#         print("很會耍帥!")
#
# dog = message1("狗")
# dog.call()
#
# year = message2("狗",12)
# year.year()
#
# sing = message3()
# sing.sing()


# 多重繼承
# class dog():# 建立類別
#     def say(self):# 建立方法
#         print("我是狗喔")
# class cate():# 建立類別
#     def say(self):# 建立方法
#         print("我是貓喔")
#
# class child(dog,cate):# 建立類別
#     pass# 省略
#
# child = child()
# child.say()# 我是狗喔

# 實際操作
# class game1():
#     name = "tony"
#     def say1(self):
#         print("看你開心哈哈哈，" + game1.name)
#
# class game2():
#     def __say(self):
#         print("看你不爽，" + game1.name)
#     def say2(self):
#         self.__say()
#
# class game3(game1,game2):
#     def copy(self):
#        super().say1()
#        super().say2()
#
# game3().copy()


