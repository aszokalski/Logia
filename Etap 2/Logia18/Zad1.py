from turtle import *

def koduj(s):
    a = 780 / (len(s) + 0.2 * (len(s) - 1))
    pu(); bk(1.2* a * len(s) / 2); pd()
    for lit in s:
        zawijas(a, suma(lit))
        
def suma(l):
    tablica = ["abcde", "fghik", "lmnop", "qrstu", "vwxyz"]
    if l is "j": l = "i"
    for i in range(len(tablica)):
        if l in tablica[i]:
            return i + 1 + tablica[i].index(l)
        
def zawijas(a, st):
    for i in range(st):
        fd(a)
        lt(90)
        a -= 4
    a += 4
    for j in range(st):
        rt(90)
        bk(a)
        a += 4
    pu()
    fd(a + a * 0.2)
    pd()
