import random

class 樂透抽獎:
    def __init__(self, 抽獎數目: int=6, 球池數目: int=48):
        self.次數 = 抽獎數目
        self.數目 = 球池數目
        self.獎號 = list()
        self.球池 = list()

    def 產生球池(self):
        self.清空球池()
        for x in range(self.數目):
            self.球池.append(x+1)

    def 清空球池(self):
        self.球池.clear()

    def 查詢球池(self):
        if len(self.球池) == 0:
            return "現在球池裡面沒有球"
        else:
            return self.球池

    def 清空獎號(self):
        self.獎號.clear()

    def 抽出一顆球(self):
        開始值 = 0
        結束值 = len(self.球池) - 1
        i = random.randint(開始值, 結束值)
        self.獎號.append(self.球池.pop(i))
        return """
        ----------------------------------------------------------------------------
        現在抽出的號碼是{}號
        """.format(self.獎號[len(self.獎號)-1])

    def 開始抽獎(self):
        if len(self.球池) == 0:
            #return "現在球池裡面沒有球"
            #return False
            self.產生球池()
        self.清空獎號()
        y = str()
        for x in range(self.次數):
            y += self.抽出一顆球()
        self.獎號.sort()
        return y

    def 查詢獎號(self):
        if len(self.獎號) == 0:
            return "現在還沒有開獎"
            return False
        return self.獎號


c = 樂透抽獎()
#c.產生球池()
print(c.開始抽獎())
print(c.查詢獎號())
