def kosp(f, s):
    cena = 0
    cont = 1
    for x, y in [f,s], [s,f]:
        for i in range(len(x)):
            if i % 2 is not 0:
                cena += int(x[i])
            elif x[i] in y:
                break
    return cena
