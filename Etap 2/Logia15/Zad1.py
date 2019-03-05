from turtle import *

def szyfr(alfabet, slowo):
    samogloski = "aeiouąęó"
    linia = dlug(len(slowo))
    pu()
    bk(linia / 2)
    pd()
    fd(linia)
    bk(linia)
    for i in range(len(slowo)):
        if slowo[i] in samogloski:
            sam = True
            rt(90)
        else:
            sam = False
            lt(90)
        fd((alfabet.index(slowo[i]) + 1) * 10)
        if sam: lt(90)
        else: rt(90)
        fd((i + 1) * 10)
        if sam: lt(90)
        else: rt(90)
        fd((alfabet.index(slowo[i]) + 1) * 10)
        if sam: rt(90)
        else: lt(90)

def dlug(n):
    wynik = 0
    add = 10
    for i in range(n):
        wynik += add
        add += 10
    return wynik
