def kk(gra):
    if gra.count('x') - gra.count('o') not in [0, -1, 1]:
        return False
    wiersze = []
    for i in range(3):
        wiersze.append(gra[i * 3 : (i + 1) * 3])
        if wiersze[i][0] is wiersze[i][1] is wiersze[i][2] is not 'w':
            return False
    for j in range(3):
        if wiersze[0][j] is wiersze[1][j] is wiersze[2][j] is not 'w':
            return False
    if wiersze[0][0] is wiersze[1][1] is wiersze[2][2] is not 'w' or wiersze[0][2] is wiersze[1][1] is wiersze[2][0] is not 'w':
        return False
    return True
    
