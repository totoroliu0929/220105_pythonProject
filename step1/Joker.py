import random
import time

class 抽鬼牌:
    def __init__(self, 名稱: str="客人", 敗場: int=0, 勝場: int=0, 平手: int=0):
        self.牌組 = [list(),list()]
        self.莊家 = [list(),list()]
        self.玩家 = [list(),list()]
        self.檢查序 = 0
        self.新一輪 = False
        self.玩家名稱 = 名稱
        self.莊家勝場 = 敗場
        self.玩家勝場 = 勝場
        self.平手場數 = 平手

    def 重新開局(self):
        self.牌組[0].clear()
        self.牌組[1].clear()
        self.莊家[0].clear()
        self.莊家[1].clear()
        self.玩家[0].clear()
        self.玩家[1].clear()
        self.檢查序 = 0
        self.新一輪 = False

    def 產生牌組(self):
        花色 = ["黑桃", "紅心", "方塊", "梅花"]
        for x in range(4):
            for y in range(1 ,14):
                self.牌組[1].append(int(y))
                if y == 1:
                    y = "A"
                elif  y == 11:
                    y = "J"
                elif  y == 12:
                    y = "Q"
                elif  y == 13:
                    y = "K"
                self.牌組[0].append(花色[x]+str(y))
        self.牌組[0].append("Joker")
        self.牌組[1].append(14)
        #return self.牌組

    def 發牌(self, 對象):
        開始值 = 0
        結束值 = len(self.牌組[0]) - 1
        x = random.randint(開始值, 結束值)
        對象[0].append(self.牌組[0].pop(x))
        對象[1].append(self.牌組[1].pop(x))
        if 對象 is self.莊家:
            print("莊家發給自己一張牌。")
        else:
            print("莊家發給你一張{}。".format(對象[0][len(對象[0]) - 1]))

    def 手牌配對(self, 對象):
        y = 對象[1][self.檢查序]
        if self.檢查序 == len(對象[1]) - 1:
            self.檢查序 = -1
        try:
            z = 對象[1].index(y, self.檢查序 + 1, len(對象[1]))
        except:
            z = 999
        if self.檢查序 == -1:
            self.檢查序 = len(對象[1]) - 1
        if z != self.檢查序 and z != 999:
            if 對象 is self.莊家:
                代稱 = "莊家"
            else:
                代稱 = "你"
            點數 = 對象[0][self.檢查序][2]
            if 點數 == "1":
                點數 = "10"
            print("「{}一對」{}扔出{}跟{}".format(點數, 代稱, 對象[0][self.檢查序], 對象[0][z]))
            if self.檢查序 == len(對象[1]) - 1:
                self.檢查序 -= 1
            對象[0].pop(z);
            對象[1].pop(z);
            對象[0].pop(self.檢查序)
            對象[1].pop(self.檢查序)
        else:
            self.檢查序 += 1
            if 對象 is self.莊家 and self.檢查序 == len(對象[1]):
                self.洗牌(對象)
                print("莊家洗一下了他手上的牌")
        return self.判定勝負(對象)

    def 判定勝負(self, 對象):
        if len(self.莊家[1]) == 0 or len(self.玩家[1]) == 0 or len(self.莊家[1]) + len(self.玩家[1]) == 3:
            if len(self.莊家[1]) == 0:
                print("莊家手上沒有牌了，莊家勝利")
                self.莊家勝場 += 1
            elif len(self.玩家[1]) == 0:
                print("你手上沒有牌了，你勝利")
                self.玩家勝場 += 1
            elif 對象 == self.莊家 and len(self.玩家[1]) == 2:
                print("莊家只剩一張牌可以讓你抽，你主動認輸了")
                self.莊家勝場 += 1
            else:
                print("你手上只剩一張牌可以讓莊家抽，莊家認輸了")
                self.玩家勝場 += 1
            self.新一輪 = True
            return "你目前是{}勝{}負{}平手".format(self.玩家勝場, self.莊家勝場, self.平手場數)
        return ""

    def 開局發牌(self):
        self.重新開局()
        self.產生牌組()
        while len(self.牌組[0])>1:
            self.發牌(self.莊家)
            self.發牌(self.玩家)
        self.發牌(self.莊家)
        print(self.確認牌組())
        self.檢查序 = 0
        while self.檢查序 < len(self.玩家[0])-1:
            self.手牌配對(self.玩家)
        self.檢查序 = 0
        while self.檢查序 < len(self.莊家[0])-1:
            self.手牌配對(self.莊家)
        return ""

    def 抽牌(self, 對象, 牌面: int=999):
        #if len(self.莊家[1]) == 0 or len(self.玩家[1]) == 0:
        #    return self.判定勝負(對象)
        #else:
        if 對象 == self.莊家:
            開始值 = 0
            結束值 = len(self.玩家[0]) - 1
            牌面 = random.randint(開始值, 結束值)
            對象[0].append(self.玩家[0].pop(牌面))
            對象[1].append(self.玩家[1].pop(牌面))
            print("莊家從你手上抽走了一張{}".format(對象[0][len(對象[0])-1]))
        elif 對象 == self.玩家:
            對象[0].append(self.莊家[0].pop(牌面))
            對象[1].append(self.莊家[1].pop(牌面))
            print("你抽到了一張{}".format(對象[0][len(對象[0]) - 1]))
        self.檢查序 = len(對象[0]) - 1
        print(self.手牌配對(對象))
        if self.新一輪 == False:
            return self.確認牌組()

    def 確認牌組(self):
        str = "你手上有{}張牌：".format(len(self.玩家[0]))
        for x in self.玩家[0]:
            str += x + "　"
        time.sleep(1)
        return str

    def 洗牌(self, 對象):
        x = [list(), list()]
        for y in range(len(對象[1])):
            開始值 = 0
            結束值 = len(對象[1]) - 1
            z = random.randint(開始值, 結束值)
            x[0].append(對象[0][z])
            x[1].append(對象[1][z])
        對象 = x

    def 開局(self):
        print(self.開局發牌())
        while self.新一輪 == False:
            try:
                print("莊家手上有{}張牌".format(len(self.莊家[0])))
                nth = int(input("你要抽莊家手上第幾張牌？"))
                if nth <= len(self.莊家[0]) and nth > 0:
                    print(self.抽牌(self.玩家, nth - 1))
                else:
                    print("莊家只有{}張牌，請輸入數字以抽牌。".format(len(self.莊家[0])))
                    continue
            except:
                print("請輸入數字以抽牌。")
            if self.新一輪 == False:
                print(self.抽牌(self.莊家))

    def 牌局(self):
        while True:
            self.開局()
            if self.新一輪 == True:
                try:
                    yn = int(input("是否再玩一次？\n1.再玩一次\n2.離開牌桌\n"))
                    if yn == 1:
                        continue
                    elif yn == 2:
                        break
                    else:
                        print("請輸入數字1或2，選擇你是否要再玩一次。")
                        continue
                except ValueError:
                    print("請輸入數字1或2，選擇你是否要再玩一次。")
                except:
                    print("請輸入數字1或2，選擇你是否要再玩一次。")
        print("你今日的戰績是{}勝{}負{}平手".format(self.玩家勝場, self.莊家勝場, self.平手場數))
        return [self.玩家勝場, self.莊家勝場, self.平手場數]

#c = 抽鬼牌()
#print(抽鬼牌().牌局())