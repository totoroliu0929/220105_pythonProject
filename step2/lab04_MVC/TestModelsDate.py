from step2.lab04_MVC.Models import Date

d = Date()
d.set(1999,12,2)
print(d)
"""
import datetime
d = datetime.datetime(2018, 5, 16)
print(d)
print('{:%m-%d-%y}'.format(d))
num = 1234567.89
print('{:,.2f}'.format(num))


name = input("請輸入姓名")
sum = score = count = 0
while (score != -1):
    score = int(input("輸入你的分數: (輸入-1結束程式)"))
    if score == -1:
        break
    sum += score
    count += 1
average = sum / count
print("%-20s, 你的平均分數是: %6.2f "%(name, average))
"""