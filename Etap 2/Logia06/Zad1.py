from turtle import *
from random import *

def siatka(s):
    a = 50
    pensize(1)
    pu(); bk(a/2 * len(s)); lt(90); bk(a/2 * 4);rt(90); pd()
    for i in range(2):
        fd(a * len(s)); lt(90); fd(a * 4); lt(90)
    for cyfra in s:
        beg = position()
        lt(90)
        if int(cyfra) < 4:
            p = randrange(4 - int(cyfra))
        else:
            p = 0
        pu()
        fd(a * p)
        rt(90)
        pd()
        zamal(a, int(cyfra))
        pu()
        goto(beg)
        fd(a)
        pd()
        

def zamal(a, n):
    fillcolor("black")
    begin_fill()
    for i in range(2):
        fd(a); lt(90); fd(a * n); lt(90)
    end_fill()
