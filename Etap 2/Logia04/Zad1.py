from turtle import *

def domki(n):
    a = 500 / len(str(n))
    pu(); bk(250); pd()
    for cyfra in str(n):
        domek(a / 2, int(cyfra))
        fd(a)
def domek(a, n):
    for i in range(4):
        troj(a)
        fd(a)
        lt(90)
        fd(a)
        lt(180)
        troj(a)
        fd(a)
        lt(90)
        fd(a)
        lt(90)
    start = position()
    lt(90)
    fd(2*a)
    rt(90)
    if n % 2 == 0:
        fillcolor("grey")
        begin_fill()
    troj(a)
    if n % 2 == 0:
        end_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(180)
    if n is 9:
        fillcolor("black")
        begin_fill()
    troj(a)
    if n is 9:
        end_fill()
    pu()
    goto(start)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    center = position()
    pd()

    fillcolor("black")
    if n in [0, 9]:
        pu(); goto(start); setheading(0); pd()
        return
    elif n in [2, 3]:
        rt(90)
    elif n in [4, 5]:
        rt(180)
    elif n in [6, 7]:
        rt(270)
        
    if n % 2 == 1:
        fd(a)
        rt(90)
        fd(a)
        rt(180)
        begin_fill()
        troj(a)
        end_fill()
    else:
        begin_fill()
        troj(a)
        end_fill()
        
    pu(); goto(start); setheading(0); pd()

def troj(a):
    start = position()
    fd(a)
    lt(90)
    fd(a)
    goto(start)
    rt(90)
    
