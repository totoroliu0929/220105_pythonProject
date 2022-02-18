import Blackjack
import Joker

class 撲克:
    def __init__(self):
        self.名稱 = "客人"
        self.莊家勝場 = 0
        self.玩家勝場 = 0
        self.平手場數 = 0

    def __str__(self):
        x = "歡迎來到這張牌桌，請問要怎麼稱呼你呢？\n"
        try:
            name = str(input(x))
            if name == "":
                print("既然你不願意透露，那我就稱呼你「客人」吧")
            else:
                self.名稱 = name
        except:
            print("既然你不願意透露，那我就稱呼你「客人」吧")
        print("{}，請問你要玩什麼撲克牌遊戲呢？".format(self.名稱))
        self.循環()
        return ""

    def 循環(self):
        中止 = False
        while True:
            try:
                game = int(input("1.21點\n2.抽鬼牌\n3.不玩\n"))
                if game == 1:
                    s = Blackjack.黑傑克(self.名稱, self.莊家勝場, self.玩家勝場, self.平手場數).牌局()
                    #self.莊家勝場 = s[0]
                    #self.玩家勝場 = s[1]
                    #self.平手場數 = s[2]
                    self.莊家勝場, self.莊家勝場, self.平手場數 = s #拆箱
                    break
                elif game == 2:
                    s = Joker.抽鬼牌(self.名稱, self.莊家勝場, self.玩家勝場, self.平手場數).牌局()
                    #self.莊家勝場 = s[0]
                    #self.玩家勝場 = s[1]
                    #self.平手場數 = s[2]
                    self.莊家勝場, self.莊家勝場, self.平手場數 = s
                    break
                elif game == 3:
                    中止 = True
                    break
                else:
                    print("什麼？{}你說的那些遊戲，因為我們開發經費有限，所以現在都還沒有，還請你多多贊助".format(self.名稱))
            except:
                print("什麼？{}你說的那些遊戲，因為我們開發經費有限，所以現在都還沒有，還請你多多贊助".format(self.名稱))
        self.結算(中止)

    def 結算(self,中止: bool=False ):
        if 中止 == False:
            print("{}，請問你要玩其他的撲克牌遊戲嗎？".format(self.名稱))
            self.循環()
        else:
            print("{}，你要離開啦，那麼，再見了".format(self.名稱))


print(撲克())