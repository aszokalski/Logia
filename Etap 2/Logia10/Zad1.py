from turtle import *

def domki(n):
    const = 1 / (2*(n - 1))
    x = n
    for j in range(n - 1):
        x -= const
    a = 450 / x
    ap = a
    pu(); bk(450 / 2); pd()
    for i in range(n):
        dom(a)
        a -= (const * ap)
def dom(a):
    fillcolor("green")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fd(a / 3)
    fillcolor("blue")
    begin_fill()
    lt(90)
    fd(a / 2)
    rt(90)
    fd(a / 3)
    rt(90)
    fd(a / 2)
    lt(90)
    bk(a / 3)
    end_fill()
    fd(a / 3)
    pu()
    bk(a / 12)
    lt(90)
    fd((7 * a)/ 12)
    rt(90)
    pd()
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        fd(a / 3)
        lt(90)
    end_fill()
    pu()
    bk(a / 2)
    pd()
    begin_fill()
    for i in range(4):
        fd(a / 3)
        lt(90)
    end_fill()
    pu()
    bk(a / 12)
    lt(90)
    fd(5 * a / 12)
    pd()
    fillcolor("red")
    begin_fill()
    rt(30)
    fd(a / 2)
    rt(60)
    fd(a / 2)
    rt(60)
    fd(a / 2)
    lt(60)
    bk(a)
    end_fill()
    lt(90)
    bk(a)
    rt(90)
    fd(a)
    
    
