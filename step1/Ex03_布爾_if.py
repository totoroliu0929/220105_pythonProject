個人資料 = [{"姓名": "John", "英文成績": 23, "數學成績": 91},
        {"姓名": "Tom", "英文成績": 96, "數學成績": 80},
        {"姓名": "Amy", "英文成績": 76, "數學成績": 82}]
print(type(個人資料))
for 個人 in 個人資料:
    總分 = 個人["英文成績"] + 個人["數學成績"]
    平均 = 總分 / 2
    if 平均 >= 90:
        評價 = "優"
    elif 平均 >= 80:
        評價 = "佳"
    elif 平均 >= 60:
        評價 = "尚可"
    else:
        評價 = "待努力"
    成績顯示 = """
姓名：{}
英文：{}
數學：{}
總分：{}
平均：{}
　　　{}
    """
    #print(f"姓名：{個人['姓名']}\n英文：{個人['英文成績']}\n數學：{個人['數學成績']}\n總分：{總分}\n平均：{平均}\n")
    print(成績顯示.format(個人['姓名'], 個人['英文成績'], 個人['數學成績'], 總分, 平均, 評價))