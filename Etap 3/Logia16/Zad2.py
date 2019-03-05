def liczby(lista):
    res = []
    for elem in lista:
        res.append(iloczyn(elem))
    return res

def iloczyn(liczba):
    para = []
    for i in range(1, liczba + 1):
        if liczba % i is 0:
            curr = [min(i, int(liczba / i)), max(i, int(liczba / i))]
            if len(para) is 0:
                para = curr
            elif para[1] - para[0] > curr[1] - curr[0]:
                para = curr
    return para
                
