def zawody(wyniki):
    zawodnicy = "ABCEDFGHIJKLMNOPQRSTUVWXYZ" [: len(wyniki[0])]
    for wynik in wyniki:
        zawodnicy = pop(zawodnicy, zawodnicy[wynik.index(min(wynik))])
    return zawodnicy
def pop(s, x):
    return s[ :s.index(x)] + s[s.index(x) + 1: ]
