from turtle import *
import turtle

def wyks(s):
    turtle.speed(0)
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    wys = 0
    szer = 0
    for litera in s:
        szer = max(szer, alfabet.index(litera) + 1)
        wys = max(wys, s.count(litera))
    pu(); bk(200); lt(90); bk(200); rt(90); pd()
    kwad(wys, szer)
    a = 400 / wys
    b = 400 / szer
    for l in alfabet[:szer + 1]:
        zamaluj(s.count(l), a, b)
        pu()
        fd(b)
        pd()
def zamaluj(n, a, b):
    fillcolor("grey")
    for i in range(n):
        begin_fill()
        for i in range(2):
            fd(b)
            lt(90)
            fd(a)
            lt(90)
        end_fill()
        if i < n:
            pu(); lt(90); fd(a); rt(90); pd()
    lt(90)
    if n > 1:
        bk(a * n)
    rt(90)
def kwad(wys, szer):
    a = 400 / wys
    b = 400 / szer
    for i in range(wys):
        for j in range(szer):
            for i in range(2):
                fd(b)
                lt(90)
                fd(a)
                lt(90)
            fd(b)
        bk(400)
        if i < wys:
            pu(); lt(90); fd(a); rt(90); pd()
    lt(90)
    if wys > 1:
        bk(400)
    rt(90)
    
