class OutputView:
    def __init__(self, list=[]):
        self.list = list

    def set(self, list):
        self.list = list

    def output(self):
        #print("{} {} {}".format(self.st.id,self.st.name,self.st.birthdate))
        print("\t\t共{}名學生".format(len(self.list)))
        for i in range(len(self.list)):
            print("\t\t{:^3}座號：{:>3} 姓名：{:<10} 生日：{}".format(i+1,self.list[i].id,self.list[i].name,self.list[i].birthdate))

    def create(self):
        print("\t\t新建立一位學生資料")
        id = input("\t\t請輸入學生座號\n\t\t")
        name = input("\t\t請輸入學生姓名\n\t\t")
        y = input("\t\t請輸入學生出生年\n\t\t")
        m = input("\t\t請輸入學生出生月\n\t\t")
        d = input("\t\t請輸入學生出生日\n\t\t")
        return id,name,y,m,d

    def menu(self):
        text = """
        請選擇您要執行的功能：
        1.顯示學生資料
        2.新建學生資料
        3.修改學生資料
        4.刪除學生資料
        5.離開
        """
        choice = input(text)
        if choice in ["1","2","3","4","5"]:
            return choice
        else:
            self.menu()

    def edit(self):
        while True:
            try:
                num = int(input("\t\t請輸入要修改的學生序號\n\t\t")) - 1
                if num < 0 or num > len(self.list):
                    print("\t\t沒有這個人")
                else:
                    print(f"\t\t修改{self.list[num].name}的資料")
                    id = input("\t\t請輸入學生座號\n\t\t")
                    name = input("\t\t請輸入學生姓名\n\t\t")
                    y = input("\t\t請輸入學生出生年\n\t\t")
                    m = input("\t\t請輸入學生出生月\n\t\t")
                    d = input("\t\t請輸入學生出生日\n\t\t")
                    return id, name, y, m, d, num
                    break
            except:
                print("\t\t沒有這個人")

    def delete(self):
        while True:
            try:
                num = int(input("\t\t請輸入要刪除的學生序號\n\t\t")) - 1
                if num < 0 or num > len(self.list):
                    print("\t\t沒有這個人")
                else:
                    print(f"\t\t刪除{self.list[num].name}的資料")
                    return num
                    break
            except:
                print("\t\t沒有這個人")