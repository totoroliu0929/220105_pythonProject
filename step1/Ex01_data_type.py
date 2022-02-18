print(100)
print(type(100))

print(0.1)
print(type(0.1))

print("100")
print(type("100"))

print(["apple", "banana", "cherry"] + ["apple1", "banana1", "cherry1"])
print(type(("apple", "banana", "cherry")))

個人資料 = [{"姓名" : "John", "英文成績" : 36 , "數學成績" : 99},
        {"姓名" : "Tom", "英文成績" : 96 , "數學成績" : 80},
        {"姓名" : "Amy", "英文成績" : 76 , "數學成績" : 82}]
print(type(個人資料))
for 個人 in 個人資料:
    總分 = 個人["英文成績"] + 個人["數學成績"]
    平均 = 總分 / 2
    print("姓名",個人["姓名"],"英文成績",個人["英文成績"],"數學成績",個人["數學成績"],"總分",總分,"平均",平均)