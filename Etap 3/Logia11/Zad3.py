def jakie(m, pytania):
    przedzialy = []
    for i in range(len(pytania) + 1):
        podzbiory = []
        for j in range(len(pytania)):

            liczba = pytania[j][0]
            odp = pytania[j][1]
            klamie = False
            
            
            if i == j:
                klamie = True

            if odp == 'w':
                if klamie:
                    podzbior = set(range(1, liczba + 1))
                else:
                    podzbior = set(range(liczba + 1, m))
            elif odp == 'm':
                if klamie:
                    podzbior = set(range(liczba, m))
                else:
                    podzbior = set(range(1, liczba))
            elif odp == 'r':
                if klamie:
                    podzbior = set(range(1, m))
                else:
                    podzbior = set([liczba, liczba])
            podzbiory.append(podzbior)
        przedzialy.append(set.intersection(*podzbiory))

    przedzialy = [[elem for elem in przedzial] for przedzial in przedzialy]
    przedzialy.sort()

    #zmiana podzbiorow na mniejsze (jak nachodzily na siebie to mniej ich bedzie)
    wynik = [[]]
    ind = 0
    processed = []
    for p in przedzialy:
        for l in p:
            if l in processed:
                continue
            processed.append(l)
            if len(wynik[ind]) == 0:
                wynik[ind].append(l)
            elif l - 1 in wynik[ind]:
                wynik[ind].append(l)
            else:
                wynik.append([l])
                ind += 1
    wynik = [[przedz[0], przedz[-1]] for przedz in wynik]
    return wynik
                
                       


