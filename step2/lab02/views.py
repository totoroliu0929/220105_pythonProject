class OutputView:
    def __init__(self):
        pass

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

    def 登記姓名(self):
        try:
            name = str(input("請問這筆投注紀錄要登記嗎？\n不想登記的話，直接按Enter繼續就可以了\n要登記的話，請輸入登記人的大名\n"))
            if name:
                self.姓名 = name
            else:
                self.姓名 = "不記名"
        except:
            pass

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