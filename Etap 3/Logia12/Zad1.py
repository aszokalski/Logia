
def sum(lista):
    res.clear()
    sumy(lista,[])
    i = 0
    while i in res:
        i+=1
    return i
res = []
def sumy(lista, liczby):
    app = 0
    for liczba in liczby:
        app += liczba
    res.append(app)
    
    if len(liczby) and liczby[-1] == lista[-1]:
        return

    for nast in lista:
        if liczby.count(nast) < lista.count(nast):
            sumy(lista, liczby + [nast])
    
