def pokolenia(lista):
    dzieci = dict()
    dz = []
    rodzic = ""
    for para in lista:
        dz.append(para[1])
        if para[0] not in dzieci.keys():
            dzieci[para[0]] = [para[1]]
        else:
            dzieci[para[0]].append(para[1])
    for r in dzieci.keys():
        if r not in dz:
            rodzic = r
    wynik = [rodzic]


    for elem in wynik:
        if type(elem) is not list:
            elem = [elem]
        pokolenie = []
        for r in elem:
            if r in dzieci.keys():
                for dz in dzieci[r]:
                    pokolenie.append(dz)
        if len(pokolenie) > 0:
            pokolenie.sort()
            wynik.append(pokolenie)

    return wynik
                
        
                
                
