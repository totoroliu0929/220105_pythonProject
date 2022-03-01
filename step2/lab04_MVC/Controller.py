from step2.lab04_MVC.Models import Date, Student, Serializer
from step2.lab04_MVC.Views import OutputView

class Controller:
    def __init__(self):
        self.data = Student.objects
        self.data.list = Serializer().deserializer()
        #self.list = self.data.data()

    def save(self):
        self.data.resort()
        Serializer().serializer(self.data.data())

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
            self.save()
        elif choice == "3":
            nid, name, y, m, d, num = OutputView(self.data.data()).edit()
            b = Date(y, m, d)
            self.data.data()[num].set(nid, name, b)
            self.save()
        elif choice == "4":
            num = OutputView(self.data.data()).delete()
            self.data.pop(num)
            self.save()
        self.go(choice)

    def go(self,choice):
        if choice != "5":
            self.run()