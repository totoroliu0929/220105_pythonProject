from step2.lab04_MVC.Models import Date, Student
hr = "\n---%-30s---"

#原始測試
print(hr%("原始測試"))
d = Date()
d.set(1999, 12, 2)
print(d)

x = []

st1 = Student()
st1.set(1, 'Amy', d)
print(st1)
x.append(st1)
print(id(x[0]),id(st1))

st2 = Student()
st2.set(2, 'Jessica', d)
print(st2)
x.append(st2)
print(id(x[1]),id(st2))

#修改d數值
print(hr%("修改d數值"))
d.set(1998)
print(d)
print(st1)
print(st2)

#修改st2數值，透過d2來修改生日
print(hr%("修改st2數值，透過d2來修改生日"))
st2.set(name="Jacky")
d2 = Date()
d2.set(2000,1,1)
st2.set(birthdate=d2)
print(st1)
print(st2)
print(id(d2))
print(id(st2.birthdate))
print(st2.birthdate.day)

#修改st2數值，直接用Date()設定1
print(hr%("修改st2數值，直接用Date()設定1"))
st2.set(birthdate=Date(9999,9,9))
print(st1)
st2 = Student() #st2已經不是原來的st2位址了
print(st2,x[1])
print(id(x[1]),id(st2))
#print(st2.birthdate.day,x[1].birthdate.day)

#修改st2數值，直接用Date()設定2
print(hr%("修改st2數值，直接用Date()設定2"))
st2.set(birthdate=Date())
print(st1)
print(st2)
print(st2.birthdate)
print(dir(st2.birthdate))
print(st2.birthdate.day)