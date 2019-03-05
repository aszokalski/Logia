
lista = []

def odj(slowo, kolejnosc):
    for e in kolejnosc:
        if e not in slowo:
            return
    dodaj = True
    for s in [slowo, slowo[::-1]]:
        wyst = []
        for elem in kolejnosc:
            wyst.append(s.index(elem))
        wystns = wyst
        wyst.sort()
        if wystns is not wyst:
            dodaj = False
            
    if dodaj and slowo not in lista:
        lista.append(slowo)
    
    for i in range(len(slowo)):
        odj(slowo[:i] + slowo[i+1:], kolejnosc)
    
def abc(slowo, kolejnosc, index):
    lista.clear()
    odj(slowo, kolejnosc)
    lista.sort()
    if index > len(lista):
        return ""
    return lista[index - 1]
