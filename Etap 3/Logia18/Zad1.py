#To jest wyszukiwanie wszerz. Uniwersalne
def droga(lista):
    polaczenia = dict()
    koszt = dict()
    stos = []
    powt = []
    for elem in lista:
        if elem[0] not in polaczenia.keys():
            polaczenia[elem[0]] = [elem[1]]
        else:
            polaczenia[elem[0]] += [elem[1]]
        if elem[1] not in polaczenia.keys():
            polaczenia[elem[1]] = [elem[0]]
        else:
            polaczenia[elem[1]] += [elem[0]]
        
    #print(polaczenia)
    stos = ['A']
    koszt['A'] = 0

    while len(stos) > 0:
        curr = stos.pop()
        if curr not in powt:
            powt.append(curr)
            #print(curr)
            nowe_polaczenia = polaczenia[curr]
            for polaczenie in nowe_polaczenia:
                stos.append(polaczenie)
                koszt[polaczenie] = koszt[curr] + 1
            if curr is 'Z':
                return koszt['Z']

    #print(koszt)
    return -1
            

#A to prosty algorytm tylko na potrzeby zadania :)                      
def droga2(lista):
    d = dict()
    for elem in lista:
        d[elem[0]] = elem[1]
        d[elem[1]] = elem[0]
    curr = 'A'
    proc = []
    res = 0
    while curr not in proc:
        proc.append(curr)
        curr = d[curr]
        res += 1
        if curr is 'Z':
            return res
    return -1
        
