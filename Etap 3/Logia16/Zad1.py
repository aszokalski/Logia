def opis(m, k):
    stolica = m[0]
    ost = {}
    rodzic = {}
    kol = []
    
    for i in range(0, len(k), 2):
        curr = k[i]
        if curr == 0:
            continue
        
        if i + 1 < len(k):
            a = k[i+1]
        if i + 2 < len(k) and k[i+2] == stolica:
            a = k[i+2]
            k[i+2] = 0

        if a != 0:
            ost[curr] = a

    poziom = 1
    for obec in m:
        if obec != stolica:
            poziom += 1
            rodzic[obec] = kol[-1]
        kol.append(obec)
        if poziom == 3:
            cel = ost[obec]
            while obec != cel and poziom > 1:
                poziom -= 1
                obec = rodzic[obec]
                kol.append(obec)
            

    #wracamy do stolicy
    while obec != stolica:
        obec = rodzic[obec]
        kol.append(obec)
    wynik = []

    for miasto in kol[::-1]:
        if miasto not in wynik:
            wynik.append(miasto)

    return wynik[::-1]
        
        
            
