import random

class 黑傑克:
    def __init__(self, 名稱: str="客人", 敗場: int=0, 勝場: int=0, 平手: int=0):
        self.牌組 = list()
        self.莊家 = list()
        self.玩家 = list()
        self.繼續 = True
        self.新一輪 = False
        self.莊家點數 = 0
        self.玩家點數 = 0
        self.玩家名稱 = 名稱
        self.莊家勝場 = 敗場
        self.玩家勝場 = 勝場
        self.平手場數 = 平手

    def 重新開局(self):
        self.牌組.clear()
        self.莊家.clear()
        self.玩家.clear()
        self.繼續 = True
        self.新一輪 = False

    def 產生牌組(self):
        花色 = ["黑桃", "紅心", "方塊", "梅花"]
        for x in range(4):
            for y in range(1 ,14):
                if y == 1:
                    y = "A"
                elif  y == 11:
                    y = "J"
                elif  y == 12:
                    y = "Q"
                elif  y == 13:
                    y = "K"
                self.牌組.append(花色[x]+str(y))
        #return self.牌組

    def 發牌(self, 對象, 首次發牌: bool=False):
        開始值 = 0
        結束值 = len(self.牌組) - 1
        抽牌 = random.randint(開始值, 結束值)
        對象.append(self.牌組.pop(抽牌))
        稱謂 = "你"
        if 對象 is self.莊家:
            稱謂 = "自己"
        if 首次發牌:
            print("莊家給了自己一張牌，蓋了起來。")
        else:
            print("莊家發給{}一張{}。".format(稱謂, 對象[len(對象) - 1]))
        self.點數計算(對象)

    def 點數計算(self, 對象):
        ace = 0
        點數 = 0
        for i in range(len(對象)):
            if 對象[i][2] == "A":
                點數 += 1
                ace += 1
            elif 對象[i][2] == "J" or 對象[i][2] == "Q" or 對象[i][2] == "K" or 對象[i][2] == "1":
                點數 += 10
            else:
                點數 += int(對象[i][2])
        if 點數 <= 11 and ace > 0:
            點數 += 10
        if 對象 is self.莊家:
            self.莊家點數 = 點數
            if self.繼續 == False and self.莊家點數 < 17:
                self.發牌(self.莊家)
            elif self.繼續 == False and self.莊家點數 >= 17:
                self.判定勝負()
        else:
            self.玩家點數 = 點數
            if self.玩家點數 >= 21:
                self.判定勝負()
        if 點數 >= 21:
            self.繼續 = False
        #print("點數", 點數)

    def 判定勝負(self):
        x = "你{}點，莊家{}點，".format(self.玩家點數, self.莊家點數)
        if self.莊家點數 > 21:
            self.玩家勝場 += 1
            print("莊家點數爆了，你勝利")
        elif self.玩家點數 > 21:
            self.莊家勝場 += 1
            print("你的點數爆了，莊家勝利")
        elif self.玩家點數 == 21 or self.莊家點數 == 21 or self.繼續 == False:
            if self.玩家點數 > self.莊家點數:
                print("{}你勝利".format(x))
                self.玩家勝場 += 1
            elif self.玩家點數 < self.莊家點數:
                print("{}莊家勝利".format(x))
                self.莊家勝場 += 1
            else:
                print("{}雙方平手".format(x))
                self.平手場數 += 1
        self.新一輪 = True
        print("你目前是{}勝{}負{}平手".format(self.玩家勝場, self.莊家勝場, self.平手場數))

    def 開局發牌(self):
        self.重新開局()
        self.產生牌組()
        for x in range(2):
            y = False
            if x == 0:
                y = True
            self.發牌(self.莊家, y)
            self.發牌(self.玩家)
        return self.確認牌組()

    def 確認牌組(self):
        str = f"莊家手上除了一張暗牌之外，還有一張{self.莊家[1]}\n你的手上則有"
        for x in self.玩家:
            str += x + "　"
        return str

    def 開局(self):
        print(self.開局發牌())
        while self.繼續:
            try:
                yn = int(input("是否繼續要牌？\n1：要牌\n2：停牌\n3:確認雙方手上的牌\n"))
                if yn ==1:
                    self.發牌(self.玩家)
                elif yn == 2:
                    self.繼續 = False
                    self.點數計算(self.莊家)
                    break
                elif yn == 3:
                    print(self.確認牌組())
                    continue
                else:
                    print("請輸入數字1-3執行你的動作。")
                    continue
            except:
                print("請輸入數字1-3執行你的動作。")

    def 牌局(self):
        while True:
            self.開局()
            if self.新一輪 == True:
                try:
                    yn = int(input("是否再來一局？\n1.再來一局\n2.離開牌桌\n"))
                    if yn == 1:
                        continue
                    elif yn == 2:
                        break
                    else:
                        print("請輸入數字1或2，選擇你是否要再來一局。")
                        continue
                except ValueError:
                    print("請輸入數字1或2，選擇你是否要再來一局。")
                except:
                    print("請輸入數字1或2，選擇你是否要再來一局。")
        print("你今日的戰績是{}勝{}負{}平手".format(self.玩家勝場, self.莊家勝場, self.平手場數))
        return [self.玩家勝場, self.莊家勝場, self.平手場數]


#c = 黑傑克()
#print(黑傑克().牌局())
