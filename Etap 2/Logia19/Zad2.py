def tram(m, n):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVW"[:m]
    przystanki = (alfabet + alfabet[1:-1][::-1]) * 2 * n
    rozklad = ""
    
    while przystanki:
        curr = przystanki[n - 1]
        #print(przystanki[:m * 2], " -- >", curr)
        rozklad += curr
        przystanki = popall(przystanki[n:], curr)

    return rozklad


def popall(slowo, x):
    ret = " "
    for lit in slowo:
        if lit != x and lit != ret[-1]:
            ret += lit
    ret = ret[1:]
    if len(ret) == 1:
        ret = ret * len(slowo)
    return ret
