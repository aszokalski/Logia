def anagramy(lista):
    wynik = []
    slista = set(lista)
    processed = []
    for slowo in lista:
        if slowo in processed:
            continue
        slowa = an(slowo)
        grupa = list(slowa & slista)
        wynik.append(grupa)
        processed += grupa
    return wynik
        

def an(slowo):
    war.clear()
    wariacjabezpowt(slowo, len(slowo), "")
    ret = war
    return set(ret)

war = []

def wariacjabezpowt(zrodlo, n, wariacja):
    if n == 0:
        war.append(wariacja)
        return

    for litera in zrodlo:
        if zrodlo.count(litera) > wariacja.count(litera):
            wariacjabezpowt(zrodlo, n - 1, wariacja + litera)
    return
        

