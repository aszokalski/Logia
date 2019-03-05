def strony(n, lista):
    kolejnosci = warkol(n)
    ret = []
    for kolejnosc in kolejnosci:
        popr = True
        for kryteria in lista:
            if kolejnosc.index(kryteria[0]) > kolejnosc.index(kryteria[1]):
                popr = False
                break
        if popr:
            ret.append(kolejnosc)
    return len(ret)
        
def warkol(n):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    war.clear()
    wariacjebezpowt(alfabet[:n], n, "")
    return war
war = []

def wariacjebezpowt(zrodlo, n, wariacja):
    if n is 0:
        war.append(wariacja)
        return

    for elem in zrodlo:
        if elem not in wariacja:
            wariacjebezpowt(zrodlo, n - 1, wariacja + elem)
    return
