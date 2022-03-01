import json
class Data:
    #因為在Student()中被引用，所以需要寫在Student()之前
    def __init__(self):
        self.list = list()

    def add(self,st):
        self.list.append(st)

    def pop(self,num):
        self.list.pop(num)

    def resort(self):
        r = sorted(self.list, key = lambda i: i.id)
        self.list = r

    def data(self):
        return self.list

class Date:
    def __init__(self, year = None, month = None, day = None):
        self.year = year
        self.month = month
        self.day = day

    def set(self, year=None, month=None, day=None):
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
        if self.id is not None:
            id = self.id if id == "" else id
        if self.name is not None:
            name = self.name if name == "" else name
        self.id = id
        self.name = name
        if self.birthdate is not None:
            year = self.birthdate.year if birthdate.year == "" else birthdate.year
            month = self.birthdate.month if birthdate.month == "" else birthdate.month
            day = self.birthdate.day if birthdate.day == "" else birthdate.day
            self.birthdate = Date(year,month,day)
        else:
            self.birthdate = birthdate

    def __str__(self):
        return f"{self.id} {self.name} {self.birthdate}"

class Serializer:
    def __init__(self):
        self.data = Data()

    def deserializer(self):
        try:
            with open("student.json") as f:
                d = json.load(f)
                for item in d:
                    b = Date(item["year"], item["month"], item["day"])
                    st = Student()
                    st.set(item["id"], item["name"], b)
                    self.data.add(st)
        except:
            pass
        finally:
            return self.data.list

    def serializer(self,nlist):
        d = list()
        for item in nlist:
            d.append({"id":item.id, "name":item.name, "year":item.birthdate.year, "month":item.birthdate.month, "day":item.birthdate.day})
        with open("student.json", "w") as f:
            json.dump(d, f)