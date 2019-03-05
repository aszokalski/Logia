def ilezmian(p, q):
    pf = p[:3]; ps = p[3:]
    qf = q[:3]; qs = q[3:]
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; alfabetB = alfabet[::-1]
    cyfry = "0123456789"; cyfryB = cyfry[::-1]
    zmiany = 0
    
    for i in range(len(pf)):
        x = alfabet.index(pf[i]) + 1
        y = alfabet.index(qf[i]) + 1
        if x > y:
            zmianyPropA = x - y
            x = alfabetB.index(pf[i]) + 1
            zmianyPropB = (x + y - 1)
            zmiany += min(zmianyPropA, zmianyPropB)
        else:
            zmiany += (y - x)
        
    for j in range(len(ps)):
        x = cyfry.index(ps[j]) + 1
        y = cyfry.index(qs[j]) + 1
        if x > y:
            zmianyPropA = x - y
            x = cyfryB.index(ps[j]) + 1
            zmianyPropB = (x + y - 1)
            zmiany += min(zmianyPropA, zmianyPropB)
        else:
            zmiany += (y - x)

    return zmiany
