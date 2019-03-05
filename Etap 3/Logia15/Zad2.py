def redukcja(tabliczka, komendy):
    n = len(tabliczka)
    for komenda in komendy:
        lista = []
        if komenda is 'l':
            lista = tabliczka
        elif komenda is 'p':
            for elem in tabliczka:
                lista.append(elem[::-1])
        elif komenda in ['g', 'd']:
            for i in range(n):
                wiersz = [tabliczka[j][i] for j in range(n)]
                if komenda is 'd':
                    wiersz = wiersz[::-1]
                lista.append(wiersz)

        for k in range(len(lista)):
            while True:
                beg = [e for e in lista[k]]
                for l in range(1, len(lista[k])):
                    if lista[k][l - 1] is 0:
                        lista[k][l - 1] = lista[k][l]
                        lista[k][l] = 0
                    elif lista[k][l - 1] is lista[k][l]:
                        lista[k][l - 1] = int(str(2 * lista[k][l])[-1])
                        lista[k][l] = 0

                if beg == lista[k]:
                    break
        newtab = []
        
        if komenda is 'l':
            newtab = lista
        elif komenda is 'p':
            for elem in lista:
                newtab.append(elem[::-1])
        elif komenda in ['g', 'd']:
            for i in range(n):
                wiersz = [lista[j][i] for j in range(n)]
                newtab.append(wiersz)
            if komenda is 'd':
                newtab = newtab[::-1]

 #       print(tabliczka, komenda, lista, newtab)
        tabliczka = newtab

    return tabliczka
                            
