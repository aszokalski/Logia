from turtle import *

def posadzka(s, w):
    if s > window_width():
        w = (window_width() *  w) / s
        s = window_width()
    elif w > window_height():
        s = (window_height() *  s) / w
        w = window_height()
    a = nwd(s, w)
    x = int(s / a)
    y = int(w / a)
    szabl = szablon(x, y)
    pu(); bk(s / 2); lt(90); bk(w / 2); rt(90); pd()
    for wiersz in szabl:
        for kol in wiersz:
            fillcolor(kol)
            pencolor(kol)
            begin_fill()
            for i in range(4):
                fd(a); lt(90)
            end_fill()
            fd(a)
        pu()
        bk(a * x)
        lt(90)
        fd(a)
        rt(90)
        pd()

def szablon(x, y):
    wiersze = []
    for i in range(y):
        if i % 2 == 0:
            wiersze.append((["black", "grey"] * x)[:x])
        else:
            wiersze.append((["grey", "black"] * x)[:x])
    return wiersze

def nwd(a, b):
    if a == b:
        return a
    else:
        return nwd(max(a, b) - min(a, b), min(a, b))
