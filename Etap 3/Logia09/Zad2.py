def szyfr(slowa):
    wynik = []
    for slowo in slowa:
        wynik.append(slimak(slowo))
    return wynik

def slimak(slowo):
    ukl = [[" " for _ in range(len(slowo))] for _ in range(len(slowo))]
    kon = [1,2,2,2] + [j for j in range(3, 20)] + [j for j in range(3, 20)]
    kon.sort()
    pivot = int(len(slowo) / 2)
    

    i = 0
    x = pivot
    y = pivot
    while len(slowo):
        elem = slowo[:kon[i]]
        for j in range(len(elem)):
            ukl[y][x] = elem[j]
            ii = i
            if j == len(elem) - 1 and i != 0:
                ii += 1
            if ii % 4 == 0:
                y += 1
            elif ii % 4 == 1:
                x += 1
            elif ii % 4 == 2:
                y -= 1
            elif ii % 4 == 3:
                x -= 1
        slowo = slowo[kon[i]:]
        i += 1

    wynik = ""
    
    for line in ukl[::-1]:
        for l in line:
            if l != ' ':
                wynik += l
    return wynik
