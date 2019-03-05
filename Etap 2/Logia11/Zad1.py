def wzorek(h, sp):
    s = []
    for letter in sp:
        s.append(letter)
    szlaczek = []
    leng = int(len(s) / h)
    for i in range(leng):
        szlaczek.append(s[h * i:h * (i + 1)])
    where = []
    print(szlaczek)
    for j in range(leng):
        currwhere = []
        for k in range(h):
            if szlaczek[j][k] == '1':
                currwhere.append([j, k])
            else:
                currwhere = []
            
        if len(where) < len(currwhere):
            where = currwhere
    most = len(where)
    for l in range(leng):
        currwhere = []
        for k in range(h):
            if szlaczek[j][k] == '1':
                currwhere.append([j, k])
            else:
                currwhere = []
            
        if  len(currwhere) == most:
            where += currwhere
    for pos in where:
        szlaczek[pos[0]][pos[1]] = '2'

    print(szlaczek)
