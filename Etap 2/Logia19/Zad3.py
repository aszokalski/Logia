def stp(pajak):
    wyniki.clear()
    stpr(pajak, 0, 1)
    return max(wyniki)

w = {
    "Z" : 0,
    "J" : 1,
    "D" : 2,
    "T" : 3
    }

wyniki = []
def stpr(zrodlo, i, lv):
    curr = zrodlo[i] 
    if curr =='Z':
        wyniki.append(lv)
        return i
    
    j = i
    for _ in range(w[zrodlo[i]]):
        j = stpr(zrodlo, j + 1, lv + 1)
    return j 

    
def stp2(pajak):

    galezie = [1]
    res = []
    for elem in pajak:
        if elem == 'Z':
            res.append(galezie[0])
        galezie = [galezie[0] + 1 for _ in range(w[elem])] + galezie[1:]
    return max(res)
