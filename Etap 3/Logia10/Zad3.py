def droga(linie, s, k):
    wynik = float('inf')

    for linia in linie:
        if s in linia and k in linia:
            nwynik = max(linia.index(s) - linia.index(k), linia.index(k) - linia.index(s))
            wynik = min(wynik, nwynik)

    return wynik

#droga([[1,2,3,4,5],[6,5,4,9,8,5,2],[1,6,5,8,9]], 1, 5)
#droga([[2,4,3,1],[4,2,1,3]], 2, 1)
#droga([[4,3,2,1],[3,2]], 2, 3)
