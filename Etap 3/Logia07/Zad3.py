
def ilemax(lista):
    war.clear()
    wariacjetrojkatow(lista, 3, [])
    trojkaty = war.copy()

    wyst = [[]for _ in range(len(trojkaty) + 1)]
    
    for liczba in lista:
        wystapienia = 0
        for trojkat in trojkaty:
            if liczba in trojkat:
                wystapienia +=1
        wyst[wystapienia].append(liczba)

    wynik = 0
    for grupa in wyst:
        wynik = max(wynik, len(grupa))
    print(wyst)
    return wynik
        

war = []
def wariacjetrojkatow(zrodlo, n, trojkat):
    if n == 0:
        trojkat.sort()
        a = trojkat[0]
        b = trojkat[1]
        c = trojkat[2]

        if trojkat not in war and a + b > c and a + c > b and c + b > a:
            war.append(trojkat)
    for liczba in zrodlo:
        if zrodlo.count(liczba) > trojkat.count(liczba):
            wariacjetrojkatow(zrodlo, n - 1, trojkat + [liczba])
    return

def ilemax2(lista):
    lista.sort()
    dlugosci = []
    for i in range(len(lista)):
        zrodlo = lista[:i]
        c = lista[i]
        dlug = 0
        proc = []
        for a, b in zip(zrodlo, zrodlo[1:] + [0]):
            if a + b > c:
                dlug += 3
            
        dlugosci.append(dlug)
        
    return max(dlugosci)
                    
