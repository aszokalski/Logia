def ms(x, zabudowane):
    teren = [[j for j in range(i + 1, i + x + 1)] for i in range(0, pow(x, 2), x)]
    wyniki = []
    most = 0
    for k in range(len(teren)):
        for l in range(len(teren[k])):
            if teren[k][l] in zabudowane: continue
            wynik = 0
            for kf in [k - 1, k + 1]:
                try:
                    if teren[kf][l] in zabudowane: wynik += 1
                except:
                    pass
            for lf in [l - 1, l + 1]:
                try:
                    if teren[k][lf] in zabudowane: wynik += 1
                except:
                    pass
            if wynik == most:
                wyniki.append(teren[k][l])
            elif wynik > most:
                most = wynik
                wyniki = []
                wyniki.append(teren[k][l])
    return wyniki
