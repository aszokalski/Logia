def kostka(gra):
    naj = []
    for elem in gra:
        if elem[1][-1] is not '6':
            continue
        if len(naj) == 0:
            naj.append(elem)
            continue
        elif len(naj[0][1]) == len(elem[1]):
            naj.append(elem)
        elif len(naj[0][1]) < len(elem[1]):
            naj = [elem]

    wynik = ["", 0]
    
    for fin in naj:
        if wynik[1] < suma(fin[1]):
            wynik = [fin[0], suma(fin[1])]
    return wynik[0]


def suma(s):
    wynik = 0
    for c in s:
        wynik += int(c)
    return wynik
