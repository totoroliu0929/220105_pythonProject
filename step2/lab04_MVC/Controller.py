from step2.lab04_MVC.Models import Date, Student, Data
from step2.lab04_MVC.Views import OutputView

class Controller:
    def __init__(self):
        self.list = Data().data()

    def run(self):
        choice = OutputView().menu()
        if choice == "1":
            OutputView(self.list).output()
        elif choice == "2":
            nid, name, y, m, d = OutputView().create()
            b = Date(y,m,d)
            st = Student()
            st.set(nid, name, b)
            self.list.append(st)
        elif choice == "3":
            nid, name, y, m, d, num = OutputView().edit(self.list)
            b = Date(y, m, d)
            st = Student()
            st.set(nid, name, b)
            self.list[num] = st
        self.go(choice)

    def go(self,choice):
        if choice != "4":
            self.run()