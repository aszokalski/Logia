def isprime(x):
    primes = [True] * (x + 1)
    for i in range(2, x + 1):
        if primes[i]:
            for j in range(2 * i, x + 1, i):
                primes[j] = False
    return primes[x]

def icp(x):
    num = 1
    for elem in x:
        num *= int(elem)
    return isprime(num)
