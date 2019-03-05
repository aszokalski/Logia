def droga(drogowskazy):
    global sprawdzone
    sasiedzi = dict()
    rodzic = dict()
    koszt = dict()
    sprawdzone = []
    
    for d in drogowskazy:
        if d[0] not in sasiedzi.keys():
            sasiedzi[d[0]] = dict()
        sasiedzi[d[0]][d[1]] = d[2]
        rodzic[d[0]] = None
        rodzic[d[1]] = d[0]
        koszt[d[0]] = float('inf')
            
        
    koszt['s'] = float('inf')
    sasiedzi['s'] = {}

    koszt['d'] = 0

    wezel = znajdznajtanszy(koszt)
    
    while wezel is not None:
        print(wezel)
        koszt_wezla = koszt[wezel]
        print("koszt obecny = ", koszt_wezla)
        sasiedzi_wezla = sasiedzi[wezel]
        print("sasiedzi = ", sasiedzi_wezla)
        print("sasiedzi:")
        for sasiad, koszt_do_sasiada in sasiedzi_wezla.items():
            print("          ", sasiad)
            nowy_koszt = koszt_wezla + koszt_do_sasiada
            print("          nowy koszt = ", nowy_koszt)
            print("          stary koszt = ", koszt[sasiad])
            if nowy_koszt < koszt[sasiad]:
                koszt[sasiad] = nowy_koszt
                rodzic[sasiad] = wezel
        sprawdzone.append(wezel)
        wezel = znajdznajtanszy(koszt)
        print("_____________________________________________________")

    print("Koszty: ", koszt)
    pt = rodzic['s']
    droga = ['s']
    while pt is not 'd':
        droga.append(pt)
        pt = rodzic[pt]
    droga = ['d'] + droga[::-1]
    print("Droga: ", droga)

    return koszt['s']

def znajdznajtanszy(k):
    wynik = [None, float('inf')]
    for elem, koszt in k.items():
        if elem not in sprawdzone and koszt < wynik[1]:
            wynik[0] = elem
            wynik[1] = koszt
    return wynik[0]
    
    
        
