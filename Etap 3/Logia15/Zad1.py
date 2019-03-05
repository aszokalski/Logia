def deszyfr(alfabet, lista):
    litera = dict()
    alfabet= " " + alfabet
    for elem in lista:
        litera[int(elem[1] / 10)] =  alfabet[int(elem[0] /10)]

    wynik = []
    curr = ""
#    print(litera)
    for i in range(1, len(lista) + 1):
        if litera[i] is " ":
            wynik.append(curr)
            curr = ""
        curr += litera[i]
    wynik.append(curr)
    return wynik
