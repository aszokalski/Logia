def obok(n, kost):
    szesc = [[[k * n**2 + j * n + i + 1 for i in range(n)] for j in range(n)] for k in range(n)]

    p = 0
    r = 0
    m = 0
    
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if szesc[a][b][c] == kost:
                    p=a
                    r=b
                    m=c
    #print(szesc[p][r][m])                  
    ret = []
    for indexy in [
        [p + 1, r, m], [p - 1, r, m],
        [p, r + 1, m], [p, r - 1, m],
        [p, r, m + 1], [p, r, m - 1]
       ]:
        if indexy[0] not in range(n) or indexy[1] not in range(n) or indexy[2] not in range(n):
            continue
        ret.append(szesc[indexy[0]][indexy[1]][indexy[2]])
    ret.sort()
    return ret
        
    
