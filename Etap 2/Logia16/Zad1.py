from turtle import *
from math import sqrt

def sze(n):
    pu(); bk(200 * sqrt(2)); lt(90); bk((5 + sqrt(2)) / 2); rt(90); pd()
    ns = str(n)
    nu = 0
    for i in range(4):
        ile = 2
        if i is 0 or i is 3:
            ile = 1
        szesc(color(nu, ns))
        nu += 1
        for i in range(ile):
            rt(30)
            fd(40)
            lt(60)
            fd(40)
            lt(60)
            fd(40)
            rt(120)
            fd(40)
            lt(30)
            szesc(color(nu, ns))
            nu += 1
        pu()
        rt(30)
        fd(40)
        rt(120)
        fd(80)
        lt(60)
        fd(40)
        lt(90)
        pd()

def color(n, l):
    if count(n, l) is 0:
        return "red"
    elif count(n, l) is 1:
        return "yellow"
    else:
        return "blue"
        
def szesc(color):
    lt(90)
    fillcolor(color)
    begin_fill()
    for j in range(6):
        fd(40)
        rt(60)
    end_fill()
    for i in range(6):
        for j in range(3):
            fd(80)
            lt(120)
        fd(40)
        rt(60)       
    rt(90)

def count(n, l):
    ile = 0
    for elem in l:
        if int(elem) is n:
            ile += 1
    print(n, " is in ", l, " ", ile, " times")
    return ile
