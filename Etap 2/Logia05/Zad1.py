from turtle import *

def grafkod(liczba):
    s = str(liczba)
    a = window_width() / len(s)
    if a * maxl(s) * 2 > window_height():
        a = window_height() / (2 * maxl(s))
    pu(); bk(len(s) * a / 2); pd()
    rt(90)
    for i in range(len(s)):
        fd(int(s[i]) * a)
        if i % 2 == 1:
            rt(90)
        else:
            lt(90)
        fd(a)
        if i % 2 == 1:
            rt(90)
        else:
            lt(90)
        fd(int(s[i]) * a)


def maxl(s):
    tab = []
    for cyfr in s:
        tab.append(int(cyfr))
    return max(tab)
