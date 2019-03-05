def nrj(rozklad):
    linie = [[], []]
    linia = dict()
    
    for autobus in rozklad:
        linie[autobus[0] - 1].append(autobus[1])
        linia[autobus[1]] = autobus[0]

    nrozklad = []
    for l in range(2):
        for i in range(0, len(linie[l]), 2):
            nrozklad.append(linie[l][i])
            if i + 1 not in range(len(linie[l])):
                break
            nautobus = srh(linie[l][i], linie[l][i+1])
            while nautobus in nrozklad:
                nautobus += 1
            for a in [nautobus, linie[l][i+1]]:
                nrozklad.append(a)
                linia[a] = l + 1
    nrozklad.sort()
    for e in range(len(nrozklad)):
        nrozklad[e] = [linia[nrozklad[e]], nrozklad[e]]
    return nrozklad
        

def srh(g1, g2):
    return mth(int((htm(g1) + htm(g2)) / 2))

def htm(godz):
    godz = str(godz)
    m = ''
    h = ''

    for minute in godz[::-1][:2][::-1]:
        m += str(minute)

    for hour in godz[::-1][2:][::-1]:
        h += str(hour)

    m = int(m)
    h = int(h)

    return 60 * h + m

def mth(minutes):
    h = minutes // 60
    m = minutes - (h * 60)
    h = str(h)
    m = str(m)
    if len(m) == 1:
        m = '0' + m
    return int(h + m)

#nrj([[1, 701], [2, 710], [1, 715], [2, 720]])
#nrj([[1, 700], [2, 707], [1, 720]])
