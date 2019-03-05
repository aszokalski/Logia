def gra(up, rundy, limit):
    boczne = {
        1 : [3,4,2,5],
        2 : [6,1,3,4],
        3 : [6,1,2,5],
        4 : [6,1,2,5],
        5 : [6,1,3,4],
        6 : [3,4,2,5]
        }

    punkty = [0 for k in range(len(rundy[0]))]
    wynik = punkty[:]
    
    for i in range(len(rundy)):
        runda = rundy[i]
        for j in range(len(runda)):
            if runda[j] == 'o':
                up = max(boczne[up])
            elif runda[j] == 'r':
                up = min(boczne[up])
            punkty[j] += up
            if punkty[j] >= limit and wynik[j] == 0:
                wynik[j] = i + 1

    return wynik
        
#gra(3, [['o', 'r'],['r', 'r'],['r', 'o']], 7)
#gra(4, [['o'],['r'],['r']], 7)
#gra(4, [['o', 'r', 'r'],['r', 'o', 'r']], 5)
