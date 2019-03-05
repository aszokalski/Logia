from turtle import *
from math import sqrt

def kodsum(n):
    skladniki = suma(n)
    a = 500 / (len(skladniki) + 1)
    pu(); bk(250); lt(90); bk(a / 2 * sqrt(2)); rt(90); pd()
    for i in range(len(skladniki)):
        cyfra(a, skladniki[i])
        if i % 2 == 0:
            pu()
            fd(2 * a)
            lt(60)
            fd(2 * a)
            lt(120)
            pd()
        else:
            pu()
            lt(60)
            fd(2 * a)
            lt(120)
            pd()
            
def cyfra(a, n):
    fillcolor("black")
    if n is 1:
        begin_fill()
    troj(a)
    if n is 1:
        end_fill()
    fd(a)
    if n is 4:
        begin_fill()
    troj(a)
    if n is 4:
        end_fill()
    lt(60)
    if n is 8:
        begin_fill()
    troj(a)
    if n is 8:
        end_fill()
    fd(a)
    lt(120)
    fd(a)
    rt(180)
    if n is 2:
        begin_fill()
    troj(a)
    if n is 2:
        end_fill()
    lt(60)
    bk(a)
    rt(60)
    
def troj(a):
    for i in range(3):
        fd(a); lt(120)
def suma(n):
    suma = 0
    skladniki = []
    while(suma != n):
        if(suma + 8 <= n):
            suma += 8
            skladniki.append(8)
        elif(suma + 4 <= n):
            suma += 4
            skladniki.append(4)
        elif (suma + 2 <= n):
            suma += 2
            skladniki.append(2)
        elif (suma + 1 <= n):
            suma += 1
            skladniki.append(1)
    return skladniki
