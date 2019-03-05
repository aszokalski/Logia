def kulki(lk):
    war.clear()
    zrodlo = 'r' * lk[0] + 'g' * lk[1] + 'b' * lk[2] + 'y' * lk[3]
    wariacjabezpowt(zrodlo, len(zrodlo), "")
    lista = war[:]
    wynik = []
    
    for w in lista:
        keep = True
        for i in range(len(w) - 1):
            if w[i] == w[i+1]:
                keep = False
                break
        if keep and w not in wynik:
            wynik.append(w)
    wynik.sort()
    return wynik
                

war = []
def wariacjabezpowt(zrodlo, n, wariacja):
    if n == 0:
        war.append(wariacja)
        return

    for litera in zrodlo:
        if wariacja.count(litera) < zrodlo.count(litera):
            wariacjabezpowt(zrodlo, n-1, wariacja+litera)
    
    return
