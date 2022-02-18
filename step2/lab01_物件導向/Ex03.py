class St:
    def __init__(self):
        self.name = None
        self.eng = None
        self.math = None

    def 修改(self, name=None, eng=None, math=None):
        self.name = name
        self.eng = eng
        self.math = math

    def 總分(self):
        tot = None
        if self.eng is not None or self.math is not None:
            tot = self.eng + self.math
        return tot

    def 顯示(self):
        tot = self.總分()
        print(self.name, self.eng , self.math, tot)

#主流程
st1 = St()
st1.修改("Tom", 99, 90)
st1.顯示()

st2 = St()
st2.修改(eng=60, math=99, name="Amy")
st2.顯示()