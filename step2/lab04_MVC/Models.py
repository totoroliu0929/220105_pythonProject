class Data:
    #因為在Student()中被引用，所以需要寫在Student()之前
    def __init__(self):
        self.list = list()

    def add(self,st):
        self.list.append(st)

    def data(self):
        return self.list

class Date:
    def __init__(self, year = None, month = None, day = None):
        self.year = year
        self.month = month
        self.day = day

    def set(self, year=None, month=None, day=None):
        year = self.year if year is None else year
        month = self.month if month is None else month
        day = self.day if day is None else day
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        if self.year is None or self.month is None or self.day is None:
            return "日期尚未設定完整"
        return f"{self.year}-{self.month}-{self.day}"

class Student:
    #類別屬性 共享資料（全域變數）
    objects = Data()

    def __init__(self):
        self.id = None
        self.name = None
        self.birthdate = None

    def set(self, id = None, name = None, birthdate = None):
        id = self.id if id is None else id
        name = self.name if name is None else name
        self.id = id
        self.name = name
        if birthdate is not None:
            self.birthdate = Date()
            self.birthdate.year = birthdate.year
            self.birthdate.month = birthdate.month
            self.birthdate.day = birthdate.day
        else:
            self.birthdate

    def __str__(self):
        return f"{self.id} {self.name} {self.birthdate}"