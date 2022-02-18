def 初值(st):
    name = None
    eng = None
    math = None
    #因為引入的st是物件，所以此處的st會指向全域變數的st，因此可以從此處做修改
    st.append(name)
    st.append(eng)
    st.append(math)

def 修改(st, name=None, eng=None, math=None):
    print(id(st))
    #st = [1, 2, 3]
    #print(id(st))
    #st = [1,2,3] #這一行重新定義了區域變數st的記憶體位址，導致這個st跟原本引入的全域變數st脫鉤,因此讓此處的修改不是修改全域變數
    st[0] = name
    st[1] = eng
    st[2] = math

def 總分(st):
    name, eng, math = st
    tot = None
    if eng is not None or math is not None:
        tot = eng + math
    return tot

def 顯示(st):
    name, eng, math = st
    tot = 總分(st)
    print(name, eng , math, tot)

#主流程
st1 = list()
初值(st1)
print(id(st1))
#顯示(st1)
修改(st1, "Tom", 99, 90)
顯示(st1)
print(st1)


st2 = list()
初值(st2)
#顯示(st2)
修改(st2, eng=60, math=99, name="Amy")
顯示(st2)
print(st2)