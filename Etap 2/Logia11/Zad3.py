def pionek(w, p, c):
    plansza = []
    dlug_rzedu = int(len(p) / w)
    ruchy = 0
    for i in range(w):
        plansza.append(p[i * dlug_rzedu : (i+ 1) * dlug_rzedu])

    wystapienia = []
    
    for j in range(len(plansza)):
        for k in range(len(plansza[j])):
            if int(plansza[j][k]) == c:
                wystapienia.append([j, k])

    for wyst in wystapienia:
        for wystin in wystapienia:
            if wyst is not wystin:
                prop = max((wyst[0] - wystin[0]) + (wyst[1] - wystin[1]), (wystin[0] - wyst[0]) + (wystin[1] - wyst[1]))
                if ruchy > prop or ruchy == 0:
                    ruchy = prop
    return ruchy
