from turtle import *
import turtle

def szyfruj(s, p):
    if p > len(s):
        a = 480 / p
    else:
        a = 760 / len(s)
    turtle.speed(0)
    pu(); bk(a / 2 * len(s)); lt(90); bk(a / 2 * p); rt(90); pd()
    for m in range(p):
        for j in range(len(s)):
            for k in range(4):
                fd(a)
                lt(90)
            fd(a)
        pu()
        bk(a * len(s))
        lt(90)
        fd(a)
        rt(90)
        pd()
    b = a / 5
    pu()
    rt(90)
    fd(b)
    lt(90)
    pd()
    for i in range(len(s)):
        litera(s[i], b)
        fd(a)
        if i % p is 0:
            lt(90)
            fd(a + b)
            rt(90)
            fd(a + b)
            lt(90)
        else:
            rt (90)
            fd(a + b)
            lt(90)
        
def litera(l, a):
    alfabet="abcdefghijklmnopqrstuvwxyz"
    n = alfabet.index(l) + 1
    siatka(a, 5, 5)
    lt(90)
    bok = 4
    x = 1
    g = 1
    w = 0
    pos = "gora"
    for i in range(n - 1):
        fillcolor("green")
        begin_fill()
        kwad(a)
        end_fill()
        if i % bok == 0 and i is not 0:
            rt(90)
            x += 1
            if x % 4 is 0:
                g += 1
                bok -= 1
            if x % 6 is 0:
                bok -= 1
        else:
            fd(a)
            if x in [1,5,9]:
                pos = "gora"
                w += 1
            elif x in [3, 7]:
                pos = "dol"
                w -= 1
            elif x in [2, 6]:
                pos = "prawo"
            elif x in [4, 8]:
                pos = "lewo"


    if pos is "gora":
        rt(90)
    elif pos is "dol":
        lt(90)
    elif pos is "lewo":
        rt(180)
    bk(g * a)
    lt(90)
    bk(w * a)
    rt(90)


def kwad(a):
    for i in range(4):
        fd(a)
        lt(90)

def siatka(a, x, y):
    for i in range(x):
        for j in range(y):
            kwad(a)
            fd(a)
        if i < x - 1:
            bk(5 * a)
            rt(90)
            fd(a)
            lt(90)
    bk((y - 1) * a)
    
