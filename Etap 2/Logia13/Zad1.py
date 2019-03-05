from turtle import *

def mozaika(a, n, s):
    if len(s) < len(a) + 1:
        b = 300 / (len(a) + 1)
    else:
        b = 600 / len(s)
    pu(); bk(b / 2 * len(s)); lt(90); bk(b / 2 * (len(a) + 1)); rt(90); pd()
    szabl = szablon(s, n, a)
    for wiersz in szabl:
        for elem in wiersz:
            fillcolor(kolor(elem))
            begin_fill()
            for i in range(4):
                fd(b)
                rt(90)
            fd(b)
            end_fill()
        pu()
        bk(b * len(s))
        lt(90)
        fd(b)
        rt(90)
        pd()
            
def kolor(k):
    if k is 'x':
        return "black"
    elif k is 'f':
        return "purple"
    elif k is 'z':
        return "green"
    elif k is 'b':
        return "white"
    
def szyfruj(s, n, a):
    ret = ""
    for elem in s:
        ret += a[(a.index(elem) + n) % len(a)]
    return ret
        
def szablon(s, n, a):
    szab = []
    szab.append(s)
    for i in range(len(a)):
        szab.append(szyfruj(szab[-1], n, a))
    return szab
