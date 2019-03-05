from math import sqrt

def lllp(n):
    liczby = threedigprimes()
    lustrzane = []
    processed = []
    for liczba in liczby:
        if liczba in processed:
            continue
        odwr = int(str(liczba)[::-1]) 
        if odwr in liczby and odwr != liczba:
            lustrzane.append(liczba)
            processed.append(odwr)
            processed.append(liczba)

    wynik = []

    i = 0
    while len(wynik) < n and i in range(len(lustrzane)):
        wynik.append(int(str(lustrzane[i]) + str(lustrzane[i])[::-1]))
        i += 1

    return wynik
    
def threedigprimes():
    p = sito(999)
    return p[p.index(101):]

def sito(n):
    isprime = [True for f in range(n + 1)]
    for d in [0,1]:
        isprime[d] = False
        
    for i in range(2, int(sqrt(n)) + 1):
        for j in range(2 * i, n + 1, i):
            isprime[j] = False

    primes = []
    for p in range(n):
        if isprime[p]:
            primes.append(p)
            
    return primes
            
