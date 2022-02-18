x = input("?")
print(x is None)
print(x == "",124)
x = [1,2,3,4]
y = 4
print(y in [1,2,3,4])
from step2.lab04_MVC.Models import Date, Student
from step2.lab04_MVC.Views import OutputView

list = []
print(list)
z = OutputView(list)
z.output()