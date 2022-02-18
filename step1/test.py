print(['22', '123']+['1234000']+['44444444', '9999'])
def order_weight(strng):
    # your code
    x = strng.split()
    if len(x) > 0:
        y = listSort(x)
    return " ".join(str(z) for z in y) if len(x) > 0 else strng


def listSort(list):
    n1 = []
    n2 = []
    n3 = []
    x = compare(list[0])
    for i in list:
        if i != list[0]:
            if compare(i) < x:
                n1.append(i)
            elif compare(i) > x:
                n2.append(i)
            else:
                for j in range(len(list[0])):
                    if i[j] is not None or i[j] < list[0][j]:
                        n1.append(i)
                    else:
                        n2.append(i)
        else:
            n3.append(i)
    if len(n1) > 1:
        n1=listSort(n1)
    if len(n2) > 1:
        n2=listSort(n2)
    print(n1,n3,n2)
    return n1 + n3 + n2

def compare(str):
    cum = 0
    for i in str:
        cum += int(i)
    return cum

print(order_weight(""))
print(order_weight('1 200 2 4 4 6 6 7 7 18 27 72 81 9 91 425 31064 7920 67407 96488 34608557 71899703'))