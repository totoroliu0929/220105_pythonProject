import random

def 樂透號碼(數量):
    x = list()
    for i in range(1, 數量+1):
        x.append(i)
    return x

def 中獎號碼(次數, 樂透號碼):
    x = list()
    for y in range(次數):
        起始值 = 0
        結束值 = len(樂透號碼)-1
        i = random.randint(起始值, 結束值)
        x.append(樂透號碼.pop(i))
        x.sort()
    return x
a = 樂透號碼(48)
print(a, len(a))
b = 中獎號碼(6, a)
print(a, len(a))
print(b, len(b))

class 球池抽獎:
    def __init__(self, 抽獎次數: int=6, 號碼數量: int=48):
        self.次數 = 抽獎次數
        self.數量 = 號碼數量
        self.球池 = list()
        self.獎號 = list()

    def 產生球池號碼(self):
        self.球池.clear()
        for i in range(1, self.數量 + 1):
            self.球池.append(i)
        return self.球池

    def 剩餘號碼(self):
        return self.球池

    def 中獎號碼(self):
        return self.獎號

    def 進行抽獎(self):
        self.獎號.clear()
        if self.數量 != len(self.球池):
            self.產生球池號碼()
        for x in range(self.次數):
            起始值 = 0
            結束值 = len(self.球池) - 1
            i = random.randint(起始值, 結束值)
            self.獎號.append(self.球池.pop(i))
        self.獎號.sort()
        return self.獎號

c = 球池抽獎()
d = c.進行抽獎()
print(d, len(d))
print(c.進行抽獎(), len(d), c.剩餘號碼(), c.中獎號碼())