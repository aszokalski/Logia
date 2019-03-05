def kolit(s):
    ile = 0
    kolumny = ["" for k in range(len(s))]
    i = 0
    while len(s) > i:
        for j in range(len(s[:i + 1])):
            kolumny[j] +=  s[:i + 1][j]
        s = s[i + 1:]
        i += 1
    for l in range(len(s)):
            kolumny[l] +=  s[l]

    for elem in kolumny:
        if elem is not "":
            add = True
            for lit in elem:
                if lit is not elem[0]:
                    add = False
            if add:
                ile += 1
    return ile
                
