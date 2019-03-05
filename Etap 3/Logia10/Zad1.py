from turtle import *
from random import shuffle

def statki():
    szablon = generuj([4,3,3,2,2,2,1,1,1,1])
    pu(); bk(200); lt(90); bk(200); rt(90); pd()
    siatka()

    breaks = [9, 18, 27, 34, 41, 46, 51]

    fillcolor("green")
    for i in range(len(szablon)):
        begin_fill()
        if szablon[i] == 1:
            for _ in range(4):
                fd(40)
                lt(90)
            end_fill()
        fd(40)

        if i in breaks:
            lt(90)
            fd(40)
    

    
def siatka():
    a = 40
    start = position()
    for _ in range(10):
        for _ in range(10):
            for _ in range(4):
                fd(a)
                lt(90)
            fd(a)
        pu()
        bk(a * 10)
        lt(90)
        fd(a)
        rt(90)
        pd()
    setpos(start)

def generuj(lista):
    shuffle(lista)
    szablon = []
    krawedzie = [10,9,9,7,7,7,5,5,5]
    krawedz = 0
    i = 0
    for statek in lista:
        krawedz += statek
        if krawedz > krawedzie[i]:
            for _ in range(krawedz - krawedzie[i]):
                szablon.append(0)
            krawedz = statek
        
        for _ in range(statek):
            szablon.append(1)
        szablon += [0,0]
        krawedz += 2
    return szablon
