def ileod(x):
    xn = int(x, 2)
    res = 0
    while not czynaprz(bin(xn)[2:]):
        xn -= 1
        res += 1
    return bin(res)[2:]

def czynaprz(x):
    for cyfra1 in x[::2]:
        if cyfra1 is not x[0]:
            return False
    for cyfra2 in x[1::2]:
        if cyfra2 is not x[1]:
            return False
    if x[0] == x[1]:
        return False
    return True
