年份 = 2100
閏年 = (年份 % 4 == 0 and 年份 % 100 != 0) or (年份 % 400 == 0)
if not 閏年:
    print("平年")
else:
    print("閏年")

class 閏年判斷:
    def __init__(self, 年份: int=2000):
        self.年份 = 年份

    def __str__(self):
        閏年 = (self.年份 % 4 == 0 and self.年份 % 100 != 0) or (self.年份 % 400 == 0)
        if not 閏年:
            判斷結果 = "平年"
        else:
            判斷結果 = "閏年"
        return "{}是{}".format(self.年份, 判斷結果)

#print(閏年判斷())
#print(閏年判斷(2001))
#print(閏年判斷(2020))
#print(閏年判斷(2022))
#print(閏年判斷(2100))


for x in range(2000, 2140, 10):
  print(閏年判斷(x))