個人資料 = [{"姓名": "John", "國文成績": 63, "英文成績": 23, "數學成績": 91},
        {"姓名": "Tom", "國文成績": 94, "英文成績": 96, "數學成績": 80},
        {"姓名": "Jessica", "國文成績": 72, "英文成績": 82, "數學成績": 56},
        {"姓名": "Amy", "國文成績": 88, "英文成績": 76, "數學成績": 82}]
print(type(個人資料))
for 個人 in 個人資料:
    總分 = 個人["國文成績"] + 個人["英文成績"] + 個人["數學成績"]
    平均 = 總分 / 3
    if 個人["國文成績"] >= 60 and 個人["英文成績"] >= 60 and 個人["數學成績"] >= 60:
        錄取 = "錄取"
    elif 個人["國文成績"] >= 90 or 個人["英文成績"] >= 90 or 個人["數學成績"] >= 90:
        錄取 = "錄取"
    else:
        錄取 = "未錄取"
    成績顯示 = """
姓名：{}
國文：{}
英文：{}
數學：{}
總分：{}
平均：{}
　　　{}
    """
    print(成績顯示.format(個人['姓名'], 個人['國文成績'], 個人['英文成績'], 個人['數學成績'], 總分, 平均, 錄取))