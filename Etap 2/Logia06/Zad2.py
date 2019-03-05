from turtle import*
from math import sqrt

def maxtr(x):
    tr = ciagfib(x)
    a = window_height() / ((len(tr) * 2 * sqrt(3)) + ((len(tr) - 1) * sqrt(3)/2))
    pu(); bk(((2 * a * tr[0]) + (a * (tr[0] - 1)))/ 2); lt(90); bk(window_height()/ 3); rt(90); pd()
    for wiersz in tr:
        pocz = position()
        for i in range(wiersz):
            szesciokat(a)
            pu()
            fd(3 * a)
            pd()
        pu()
        goto(pocz)
        lt(90)
        fd(a * sqrt(3))
        rt(90)
        fd(1.5 * a)
        lt(90)
        fd(a * sqrt(3) / 2)
        rt(90)
        pd()
def ciagfib(n):
    ciag = [1]
    suma = 1
    while suma <= n:
        suma += ciag[-1] + 1
        if suma <= n:
            ciag.append(ciag[-1] + 1)
    return ciag[::-1]

def szesciokat(a):
    pu(); fd(a / 2); pd();
    fillcolor("black")
    begin_fill()
    for i in range(6):
        fd(a)
        lt(60)
    end_fill()
    pu(); bk(a / 2); pd();
