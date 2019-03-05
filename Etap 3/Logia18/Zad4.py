from math import sqrt

def dzielniki(a, b):
    lista = []
    #najpierw napisałem powolną funkcję liczącą ilość dzielników każdej liczby ze zbioru <a, b>.
    #Zauważyłem, że wyniki są kwadratami liczb pierwszych.
    pr = pierwsze(int(sqrt(b)) + 1)
    for liczba in range(a, b + 1):
        if sqrt(liczba) in pr:
            lista.append(liczba)
        
    return len(lista)

def pierwsze(n):
    prime = [True] * (n + 1)
    ret = []
    for i in range(2, int(sqrt(n)) + 1):
        for j in range(2 * i, n + 1, i):
            prime[j] = False

    for k in range(2, n + 1):
        if prime[k]:
            ret.append(k)
    return ret
        
