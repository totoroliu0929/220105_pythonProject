def order_weight(strng):
    # your code
    return ' '.join(
        sorted(
            sorted(strng.split(' ')),
            key=lambda x: sum(int(c) for c in x)
        )
    )

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
                    if len(i) < j + 1 or i[j] < list[0][j]:
                        n1.append(i)
                        break
                    elif i[j] > list[0][j] or j == len(list[0])-1:
                        n2.append(i)
                        break
        else:
            n3.append(i)
    if len(n1) > 1:
        n1=listSort(n1)
    if len(n2) > 1:
        n2=listSort(n2)
    return n1 + n3 + n2

def compare(str):
    cum = 0
    for i in str:
        cum += int(i)
    return cum

print(order_weight(""))
print(order_weight('200 200 3 112 14 14 132 151 16 160 162 162 171 18 45 63 173 174 174 320142 86 95 87 88 179 188 71441 416125 211376 347015 417170 6545 136551 57126 182902 264604 450373 13946 328145 257426 367830 228826 443882 176295 71859 133798 347648 389543 163789 148796'))