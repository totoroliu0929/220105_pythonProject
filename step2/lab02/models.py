class Data:
    def __init__(self):
        self.姓名 = str()
        self.選號 = list()
        self.投注紀錄 = dict()
        self.開獎紀錄 = dict()
        self.頭獎 = dict()
        self.期數 = int(1)

    def 讀取開獎紀錄(self):
        try:
            with open("lotto.json") as f:
                self.開獎紀錄 = json.load(f)
        except FileNotFoundError:
            self.開獎紀錄 = dict()
        except:
            self.開獎紀錄 = dict()
        if len(self.開獎紀錄) != 0:
            self.期數 = int(list(self.開獎紀錄.keys())[len(self.開獎紀錄)-1]) + 1

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