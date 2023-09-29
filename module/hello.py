# 製作個人模組
class hello1():
    def __init__(self,name):
        self.name = name
    def say1(self):
        if self.name == "寶貝":
            print("老公，你最好了")
        else:
            print("你吃屎八")
class hello2(hello1):
    def __init__(self,name):
        super().__init__(name)
    def say2(self):
        super().say1()

