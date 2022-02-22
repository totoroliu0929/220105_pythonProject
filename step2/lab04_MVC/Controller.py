from step2.lab04_MVC.Models import Date, Student
from step2.lab04_MVC.Views import OutputView

class Controller:
    def __init__(self):
        self.data = Student.objects
        #self.list = self.data.data()

    def run(self):
        choice = OutputView().menu()
        if choice == "1":
            OutputView(self.data.data()).output()
        elif choice == "2":
            nid, name, y, m, d = OutputView().create()
            b = Date(y,m,d)
            st = Student()
            st.set(nid, name, b)
            self.data.add(st)
            self.data.resort()
        elif choice == "3":
            nid, name, y, m, d, num = OutputView(self.data.data()).edit()
            b = Date(y, m, d)
            self.data.data()[num].set(nid, name, b)
            self.data.resort()
        elif choice == "4":
            num = OutputView(self.data.data()).delete()
            self.data.pop(num)
        self.go(choice)

    def go(self,choice):
        if choice != "5":
            self.run()