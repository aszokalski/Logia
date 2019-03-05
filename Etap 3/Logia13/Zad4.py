def maxj(lista):
    nlista = [[0 for lat in elem] for elem in lista]
    n = len(lista)
    for i in range(n):
        m = len(lista[i])
        for j in range(m):
            nlista[i][j] += lista[i][j]
            war2 = lista[i][j] / 2
            war3 = lista[i][j] /3
            
            if i - 1 in range(n):
                nlista[i-1][j] += war2
                if j - 1 in range(m):
                   nlista[i-1][j-1] += war3
                if j + 1 in range(m):
                   nlista[i-1][j+1] += war3
            if i + 1 in range(n):
                nlista[i+1][j] += war2
                if j - 1 in range(m):
                    nlista[i+1][j-1] += war3
                if j + 1 in range(m):
                    nlista[i+1][j+1] += war3
            if j - 1 in range(m):
               nlista[i][j-1] += war2
            if j + 1 in range(m):
               nlista[i][j+1] += war2
    res = [0,0]
    for k in range(n):
        for l in range(len(nlista[k])):
            if nlista[k][l] > nlista[res[0]][res[1]]:
                res = [k, l]
    res[0] += 1
    res[1] += 1
    return res
