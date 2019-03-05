from turtle import *

def rysuj(s):
    a = 720 / len(s)
    up = "bdfhklt"
    down = "gjpqy"
    numb = "0123456789"
    samogloski = "aeiouy"
    pu(); bk(360); pd()
    for elem in s:
        if elem in numb:
            prost(a, "green")
        elif elem in up:
            prost(a, "yellow")
        elif elem in down:
            col = "yellow"
            if elem in samogloski:
                col = "red"
            pu(); rt(90); fd(a); lt(90); pd()
            prost(a, col)
            pu(); lt(90); fd(a); rt(90); pd()
        else:
            col = "yellow"
            if elem in samogloski:
                col = "red"
            kwad(a, col)
            
def prost(a, col):
    fillcolor(col)
    begin_fill()
    for i in range(2):
        fd(a)
        lt(90)
        fd(2 * a)
        lt(90)
    fd(a)
    end_fill()

def kwad(a, col):
    fillcolor(col)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    fd(a)
    end_fill()
