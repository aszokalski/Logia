from math import sqrt

def sumDziel(n):
    suma = 0
    for i in range(1, n):
        if(n % i == 0):
            suma += i
    return suma

def ilepd(m, n):
    wynik = 0
    for i in range(m, n + 1):
        if(i % sumDziel(i) == 0):
            wynik += 1
    return wynik
        
