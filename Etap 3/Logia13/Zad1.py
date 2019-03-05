def kulki(podstawa):
    c = podstawa.count('c')
    z = podstawa.count('z')
    tail = ""
    
    if c < z:
        tail = (z - c) * 'z'
    elif c > z:
        tail = (c - z) * 'c'

    cel = "cz" * min(c, z) + tail

wyn = []
def zamiany(zrodlo, cel, zamiana):
    if zrodlo == cel:
        wyn.append(zamiana)
        return
    elif zamiana > len(zrodlo):
        return

    for i in range(len(zrodlo)):
        for j in range(len(zrodlo)):
            if zrodlo[i] is not zrodlo[j]:
                zamiany(zrodlo[:min(i, j)] + zrodlo[max(i, j)] + zrodlo[min(i, j) + 1: max(i, j)] + zrodlo[min(j, i)] + zrodlo[max(i, j) + 1:], cel, zamiana + 1)
