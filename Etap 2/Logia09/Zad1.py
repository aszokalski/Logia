from turtle import*
from math import sqrt

def czekoladka(slowo):
    a = 2800 / (5 * (len(slowo) - 1))
    lt(90)
    rt(90)
    trojkat(30)

def letter(a, pattern):
    if pattern[0] == 'p':
        for i in range(4):
            if pattern[i] == '1':
                pd()
            if i == 0 or i == 2:
                fd(a / 2)
            else:
                fd(a)
            rt(90)
            pu()
        pu()
        fd(a / 4)
        rt(90)
        if pattern[4] == 'l':
            fd(a / 4)
        elif pattern[4] == 'p':
            fd(a - (a / 4))
        dot(a / 6)
    elif pattern[0] == 't':
        

def trojkat(a):
    pu()
    lt(90)
    fd(a)
    rt(135)
    pd()
    fd((a) * sqrt(2))
    lt(90)
    fd((a) * sqrt(2))
    pu()
    rt(135)
    fd(a)
    lt(90)
    
    
    
