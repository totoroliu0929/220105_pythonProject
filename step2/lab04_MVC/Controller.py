from step2.lab04_MVC.Models import Date, Student
from step2.lab04_MVC.Views import OutputView

class Controller:
    def __init__(self):
        self.data = Student.objects
        self.list = self.data.data()

    def run(self):
        choice = OutputView().menu()
        if choice == "1":
            OutputView(self.list).output()
        elif choice == "2":
            nid, name, y, m, d = OutputView().create()
            b = Date(y,m,d)
            st = Student()
            st.set(nid, name, b)
            self.data.add(st)
        elif choice == "3":
            nid, name, y, m, d, num = OutputView(self.list).edit()
            b = Date(y, m, d)
            self.list[num].set(nid, name, b)
        elif choice == "4":
            num = OutputView(self.list).delete()
            self.data.pop(num)
        self.go(choice)

    def go(self,choice):
        if choice != "5":
            self.run()