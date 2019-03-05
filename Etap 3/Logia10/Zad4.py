def robot(trasa):
    odcinki = []
    wynik = []
    pozycja = [0,0]
    odcinek = []
    for komenda in trasa:
        odcinek= [pozycja[:]]
        if komenda == 'N':
            pozycja[1] += 1
        elif komenda == 'S':
            pozycja[1] -= 1
        elif komenda == 'E':
            pozycja[0] += 1
        elif komenda == 'W':
            pozycja[0] -= 1
        odcinek.append(pozycja[:])
        odcinki.append(odcinek[:])

    for odc in odcinki:
        if odcinki.count(odc) + odcinki.count(odc[::-1]) >= 2 and odc not in wynik and odc[::-1] not in wynik:
            wynik.append(odc)
    return len(wynik)

#robot("NESW") -> 0
#robot("NESWNESW") -> 4
#robot("NNNESSSSWNNNE") -> 2
