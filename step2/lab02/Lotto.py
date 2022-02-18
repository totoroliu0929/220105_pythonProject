import random
import time
import json

class Lotto:
    def __init__(self):
        self.姓名 = str()
        self.選號 = list()
        self.投注紀錄 = dict()
        self.開獎紀錄 = dict()
        self.頭獎 = dict()
        self.期數 = int(1)

    def 讀取紀錄(self):
        self.讀取開獎紀錄()
        self.讀取投注紀錄()

    def 讀取開獎紀錄(self):
        try:
            with open("lotto.json") as f:
                self.開獎紀錄 = json.load(f)
        except FileNotFoundError:
            self.開獎紀錄 = dict()
        except:
            self.開獎紀錄 = dict()
        #print(self.開獎紀錄)
        if len(self.開獎紀錄) != 0:
            self.期數 = int(list(self.開獎紀錄.keys())[len(self.開獎紀錄)-1]) + 1
        #print("期數",self.期數 )

    def 讀取投注紀錄(self,期數 = None):
        期數 = self.期數 if 期數 is None else 期數
        try:
            with open(f"lotto-{期數}.json") as f:
                self.投注紀錄 = json.load(f)
        except FileNotFoundError:
            self.投注紀錄 = dict()
        except:
            self.投注紀錄 = dict()

    def 寫入開獎紀錄(self):
        self.開獎紀錄[str(self.期數)] = self.頭獎
        #self.期數如果不轉換成str，存成json時，會自動轉換成str，之後讀取時會因格式發生問題
        with open(f"lotto.json", "w") as f:
            #d = json.dumps(self.投注紀錄)
            #f.write(d)
            json.dump(self.開獎紀錄,f)

    def 寫入投注紀錄(self):
        with open(f"lotto-{self.期數}.json", "w") as f:
            #d = json.dumps(self.投注紀錄)
            #f.write(d)
            json.dump(self.投注紀錄,f)

    def 開局(self):
        print("歡迎光臨投注站")
        self.循環選項()
        print("謝謝光臨")

    def 循環選項(self):
        繼續 = True
        while True:
            try:
                詢問 = f"第{self.期數}期大樂透開放投注中\n請問你要：\n1.自己選號\n2.電腦選號\n3.查詢投注紀錄\n4.等待開獎"
                if self.檢查開獎() is False:
                    詢問 = f"第{self.期數}期已開獎，請問你要：\n3.查詢投注紀錄"
                select = int(input(f"{詢問}\n5.查詢過去紀錄\n6.離開\n"))
                if select == 1 and self.檢查開獎():
                    self.自己選號()
                    break
                elif select == 2 and self.檢查開獎():
                    self.電腦選號()
                    break
                elif select == 3:
                    self.查詢紀錄()
                    break
                elif select == 4 and self.檢查開獎():
                    self.電腦選號(True)
                    break
                elif select == 5:
                    self.驗證期數()
                    break
                elif select == 6:
                    繼續 = False
                    break
                else:
                    print("你輸入的數字不可選，請輸入其他數字。")
            except:
                print("請輸入數字選擇。")
        if 繼續:
            self.循環選項()

    def 自己選號(self):
        選號 = list()
        for x in range(6):
            while True:
                try:
                    y = int(input("請輸入你要的第{}個號碼：".format(x+1)))
                    if y in 選號:
                        print(f"{y}已經選過了")
                    elif y>0 and y<50:
                        選號.append(y)
                        break
                    else:
                        print("請輸入數字1到49")
                except:
                    print("請輸入數字1到49")
        self.紀錄投注(選號)

    def 電腦選號(self, 開獎: bool = False):
        特別號 = 0
        if 開獎:
            特別號 = 1
        選號 = self.抽出號碼(6+特別號)
        if 開獎:
            self.進行開獎(選號)
        else:
            print(選號)
            self.紀錄投注(選號)

    def 抽出號碼(self, 數量):
        選號 = list()
        while len(選號) < (數量):
            開始值 = 1
            結束值 = 49
            號碼 = random.randint(開始值, 結束值)
            if 號碼 in 選號:
                continue
            else:
                選號.append(號碼)
        return 選號

    def 紀錄投注(self, 選號):
        print(f"你選擇的號碼是{選號}")
        self.讀取投注紀錄()
        self.登記姓名()
        if self.姓名 not in self.投注紀錄:
            self.投注紀錄[self.姓名] = list()
        self.投注紀錄[self.姓名].append(選號)
        self.寫入投注紀錄()

    def 登記姓名(self):
        try:
            name = str(input("請問這筆投注紀錄要登記嗎？\n不想登記的話，直接按Enter繼續就可以了\n要登記的話，請輸入登記人的大名\n"))
            if name:
                self.姓名 = name
            else:
                self.姓名 = "不記名"
        except:
            pass

    def 進行開獎(self, 選號):
        print("隨著時間的流逝，樂透開獎的時間終於到了！\n那麼誰是本期的幸運得主呢？")
        for i in range(len(選號)):
            time.sleep(1)
            if i < 6:
                show = f"第{i+1}個獎號"
            else:
                show = "最後的特別號"
            print(f"{show}要開出來了！開出來的是：")
            time.sleep(1)
            print(選號[i])
        time.sleep(1)
        特別號 = 選號.pop()
        選號.sort()
        self.頭獎["一般號"] = tuple(選號)
        self.頭獎["特別號"] = 特別號
        print(f"\n本期的樂透已經開出，號碼是\n{self.頭獎}")
        self.寫入開獎紀錄()
        self.檢查得主()

    def 檢查得主(self):
        顧客 = self.投注紀錄.keys()
        得主 = {6:0, 15:0, 5:0, 14:0, 4:0, 13:0, 12:0, 3:0}
        for x in 顧客:
            for y in self.投注紀錄[x]:
                結果 = self.對獎(y,True)
                if 結果 in 得主:
                    得主[結果] += 1
        if 得主[6] > 0:
            print("賀！本投注佔開出頭獎！")
        if 得主[15] > 0:
            print("賀！本投注佔開出貳獎！")
        print("本投注站共開出頭獎{}注，貳獎{}注，参獎{}注，肆獎{}注，伍獎{}注，陸獎{}注，柒獎{}注，普獎{}注\n".format(*得主.values()))

    def 檢查開獎(self):
        #if len(self.頭獎) > 0:
        if len(self.開獎紀錄) > 0 and self.期數 == int(list(self.開獎紀錄.keys())[len(self.開獎紀錄)-1]):
            return False
        return True

    def 驗證期數(self):
        try:
            期數 = int(input("請輸入您要查詢的期數\n"))
            if 期數 == self.期數 and self.檢查開獎():
                print("本期尚未開出")
            elif 期數 > self.期數:
                print(f"現在才第{self.期數}期，要是我能讓你對獎的話，我不會來賣樂透了啦")
            else:
                self.查詢紀錄(str(期數))
        except:
            print("請你說阿拉伯數字好嗎？")

    def 查詢紀錄(self,期數 = None):
        期數 = str(self.期數) if 期數 is None else 期數
        self.讀取投注紀錄(期數)
        try:
            name = str(input("請問你要查詢的紀錄名稱是？\n"))
            if name == "不記名":
                print("我不能透露不記名者的投注紀錄喔！")
            elif name in self.投注紀錄:
                print("{}的話，總共有{}筆紀錄喔，分別是：".format(name, len(self.投注紀錄[name])))
                for r in self.投注紀錄[name]:
                    號碼 = ("　".join(str(x) for x in r[0:len(r)]))
                    結果 = str()
                    if self.檢查開獎() is False or int(期數) < self.期數:
                        self.頭獎 = self.開獎紀錄[期數]
                        結果 = self.對獎(r)
                    print(號碼,結果)
            else:
                print("沒有這個資料喔！")
        except:
            print("沒有這個資料喔！!")

    def 對獎(self, 號碼, 統計: bool=False):
        得獎 = {6:"頭獎", 15:"貳獎", 5:"参獎", 14:"肆獎", 4:"伍獎", 13:"陸獎", 12:"柒獎", 3:"普獎"}
        命中 = 0
        for x in 號碼:
            if x in self.頭獎["一般號"]:
                命中 += 1
            elif x ==  self.頭獎["特別號"]:
                命中 += 10
        if 統計:
            return 命中
        if 命中 in 得獎:
            return f"恭喜得了{得獎[命中]}"
        else:
            return "沒中獎"

    def 主流程(self):
        self.讀取紀錄()
        self.開局()

#lo1 = Lotto()
#lo1.主流程()