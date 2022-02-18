簡易列表 = ["a", "b", "c", "d"]
嚴謹列表 = list(("a", "b", "c", "d"))
print(簡易列表, type(簡易列表))
print(嚴謹列表, type(嚴謹列表))

嚴謹列表.append("e")
print(嚴謹列表)
嚴謹列表.insert(0, "x")
print(嚴謹列表)
嚴謹列表.remove("x")
print(嚴謹列表)
嚴謹列表.pop(3)
print(嚴謹列表)