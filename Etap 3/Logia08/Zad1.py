from turtle import *
from math import sqrt

def domino(opis):
    uklad = opis[0]
    for e in opis[1:-1]:
        if uklad[-1] + e in uklad or e + uklad[-1] in uklad:
            return "Błąd"
        uklad += 2 * e
    if uklad[-1] + opis[-1] in uklad or opis[-1] + uklad[-1] in uklad:
        return "Błąd"
    uklad += opis[-1]

    a = 400 / len(uklad)
    pu(); bk(400/2); lt(90); bk(a / 2); rt(90); pd()
    for elem in uklad:
        klocek(a, int(elem))

def klocek(n, x):
    for i in range(4):
        fd(n)
        lt(90)

    fd(n)
    end = position()
    bk(n)
    if x == 0:
        setpos(end)
        return
    if x == 1:
        pu(); fd(n/2); lt(90); fd(n/2); dot(n / 8); rt(90)
        setpos(end)
        pd()
        return
    if x == 2:
        pu(); fd(3/4 * n); lt(90); fd(1/4 * n); dot(n / 8); fd(2/4 * n); lt(90); fd(2 / 4 * n); rt(180); dot(n / 8)
        setpos(end)
        pd()
        return
    if x == 3:
        pu(); fd(3/4 * n); lt(90); fd(1/4 * n); dot(n / 8); lt(45); fd(1 / 4 * n * sqrt(2)); dot(n / 8); fd(1 / 4 * n * sqrt(2)); dot(n / 8);  rt(135)
        setpos(end)
        pd()
        return
    if x == 4:
        pu(); lt(90); fd(1/4 * n); rt(90); fd(1/4 * n); dot(n / 8); fd(1 / 2 * n); dot(n / 8); lt(90); fd(1 / 2 * n); dot(n / 8); lt(90); fd(1 / 2 * n); dot(n / 8); rt(180)
        setpos(end)
        pd()
        return
    if x == 5:
        pu(); lt(90); fd(1/4 * n); rt(90); fd(1/4 * n); dot(n / 8); fd(1 / 2 * n); dot(n / 8); lt(90); fd(1 / 2 * n); dot(n / 8); lt(90); fd(1 / 2 * n); dot(n / 8); rt(45); bk(1 / 4 * n * sqrt(2)); dot(n / 8); rt(135)
        setpos(end)
        pd()
        return
    if x == 6:
        pu(); lt(90); fd(1/4 * n); rt(90);
        for i in range(3):
            fd(1/4 * n); dot(n / 8);
        fd(1/4 * n); lt(90); fd(1/2 * n); lt(90)
        for j in range(3):
            fd(1/4 * n); dot(n / 8);
        rt(180)
        setpos(end)
        pd()
        return
    
