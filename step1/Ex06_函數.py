def 閏年判斷(年份):
    閏年 = (年份 % 4 == 0 and 年份 % 100 != 0) or (年份 % 400 == 0)
    if not 閏年:
        判斷結果 = "平年"
    else:
        判斷結果 = "閏年"
    return "{}是{}".format(年份, 判斷結果)

for x in range(2000, 2140, 10):
  print(閏年判斷(x))