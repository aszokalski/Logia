def neon(n):
    wynik = 0
    for i in range(len(n)):
        for j in range(len(n)):
            if i is j:
                continue
            ocena = max(i - j, j - i) * 2 + n[j] + n[i]
            if ocena > wynik:
                wynik = ocena
    return wynik
            
