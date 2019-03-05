def neon(neony):
    wynik = 0

    for i in range(len(neony)):
        rzad = neony[i]
        for j in range(len(rzad)):
            ocena = 0
            for k in range(len(rzad)):
                if k is j:
                    continue
                curr = max(k - j, j - k) * 2 + rzad[j] + rzad[k]
                ocena = max(ocena, curr)
            for l in range(len(neony)):
                if l is i:
                    continue
                curr = max(l - i, i - l) * 2 + neony[i][j] + neony[l][j]
                ocena = max(ocena, curr)
            wynik = max(ocena, wynik)

    return wynik
