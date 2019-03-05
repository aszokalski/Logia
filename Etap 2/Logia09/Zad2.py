def primes(p, n):
    primes = [True] * (n + 1)
    primeslist = []
    primes[0] = False
    primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    for k in range(p, n + 1):
        if primes[k]:
            primeslist.append(k)
    return primeslist

def llpp(pocz, kon):
    if pocz <= 2:
       pocz = 3
    count = int(len(primes(pocz, kon)) - 1)
    return count
    
