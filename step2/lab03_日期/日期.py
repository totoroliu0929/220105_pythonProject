class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def 修改(self, year=None, month=None, day=None):
        year = self.year if year is None else year
        month = self.month if month is None else month
        day = self.day if day is None else day
        self.year = year
        self.month = month
        self.day = day

    def 顯示(self):
        if self.year is None or self.month is None or self.day is None:
            return "日期尚未設定完整"
        return f"{self.year} {self.month} {self.day}"