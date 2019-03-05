from turtle import *

def kod(opis):
    alfabet = "ABCDEFGHIJKLM"
    ost_lit = max([alfabet.index(l) + 1 for l in alfabet if l in opis])
    ost_num = max([n for n in range(1, 27) if str(n) in opis])
    a = 468 / ost_num
    pu(); bk(a * ost_lit / 2); rt(90); bk(a * ost_num / 2); lt(90); pd()
    for i in range(1, ost_num + 1):
        szabl = [0 for _ in range(ost_lit)]
        if str(i) in opis:
            j = opis.index(str(i)) + 1
            if i >= 10:
                j += 1
            while j < len(opis) and opis[j] in alfabet:
                szabl[alfabet.index(opis[j])] = 1
                j += 1
        row(szabl, a)


def row(szabl, a):
    for elem in szabl:
        fillcolor("black")
        if elem == 1:
            begin_fill()
        for _ in range(4):
            fd(a)
            rt(90)
        if elem == 1:
            end_fill()
        fd(a)
    bk(len(szabl) * a)
    pu(); rt(90); fd(a); lt(90); pd()
