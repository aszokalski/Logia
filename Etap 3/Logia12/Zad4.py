def euro(b, m, c):
    czas = dict()
    mecze = dict()
    baza = dict()

    wynik = ['', float('inf')]
    for baz in b:
        baza[baz[0]] = baz[1]
    for mecz in m:
        if mecz[0] not in mecze.keys():
            mecze[mecz[0]] = [mecz[2]]
        else:
            mecze[mecz[0]].append(mecz[2])

        if mecz[1] not in mecze.keys():
            mecze[mecz[1]] = [mecz[2]]
        else:
            mecze[mecz[1]].append(mecz[2])
            
    for polaczenie in c:
        czas[repr(polaczenie[:2])] = int(polaczenie[2])
        czas[repr(polaczenie[:2][::-1])] = int(polaczenie[2])

    
    for druzyna, mlist in mecze.items():
        podroze = 0
        kwatera = baza[druzyna]
        
        for me in mlist:
            if me == kwatera:
                continue
            podroze += czas[repr([kwatera, me])]

        if podroze < wynik[1]:
            wynik[0] = druzyna
            wynik[1] = podroze
            
    return wynik[0]

#euro([['A', 'M1'],['B', 'M2'],['C', 'M1'],['D', 'M3']], [['A', 'B', 'M1'],['A', 'C', 'M1'],['A', 'D', 'M3'],['B', 'C', 'M1'],['B', 'D', 'M3'],['C', 'D', 'M3']], [['M1', 'M2', '1'],['M1', 'M3', '5'], ['M2', 'M3', '6']])
#euro([['D1', 'M1'],['D2', 'M2'],['D3', 'M3'],['D4', 'M4']], [['D1', 'D3', 'M5'],['D2', 'D4', 'M6'],['D1', 'D2', 'M5'],['D3', 'D4', 'M6'],['D1', 'D4', 'M5'],['D2', 'D3', 'M6']], [['M1', 'M5', '20'],['M1', 'M6', '5'],['M2', 'M5', '15'],['M2', 'M6', '10'],['M3', 'M5', '25'], ['M3', 'M6', '20'], ['M4', 'M5', '20'],['M4', 'M6', '20']])
