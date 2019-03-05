def ilen(n, mapa):
    pole = [[1 for i in range(n)] for j in range(n)]

    for obsz in mapa:
        
        x = obsz[:2] [::-1]
        y = obsz[2:4]
        y = [y[1] - 1, y[0] - 1]
        poziom = obsz[4]

        wiersz = range(x[1], y[1] + 1)
        wiersze = range(x[0], y[0] + 1)

        for k in wiersze:
            for l in wiersz:
                pole[k][l] = poziom

    wynik = [0,0,0]
    
    for w in pole:
        #print(w)
        for elem in w:
            wynik[elem-1] += 1

    return wynik
        
        
#ilen(4, [[0,0,1,2,2],[0,1,3,2,2],[3,3,4,4,3]]) -> [11,4,1]
#ilen(4, [[0,0,4,4,2]]) -> [0,16,0]
#ilen(3, [[0,0,1,1,3],[2,2,3,3,2]]) -> [7,1,1]
