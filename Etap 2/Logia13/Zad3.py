def pascal(w, p):
    trojkat = [[0 for i in range(j)] for j in range(1, w + 1)]
    for k in range(len(trojkat)):
        trojkat[k][0] = 1
        trojkat[k][-1] = 1
    for l in range(len(trojkat)):
        for m in range(len(trojkat[l])):
            if trojkat[l][m] == 0:
                trojkat[l][m] = trojkat[l - 1][m - 1] + trojkat[l - 1][m]

    return trojkat[w-1][p - 1]
