from turtle import *

def szyfruj(s):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    szyfr = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "abaaa", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab", "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb", "baabb", "babaa", "babab", "babba", "babbb"]
    if len(s) > 5:
        a = 700 / len(s)
    else:
        a = 400 / 5
    pu(); bk(a * len(s) / 2); rt(90); bk(a * 5 / 2); lt(90); pd()
    for lit in s:
        litera(szyfr[alfabet.index(lit)][::-1], a)
        
def litera(k, a):
    for i in range(5):
        if k[i] == "a": c = "yellow"
        else: c = "blue"
        fillcolor(c)
        begin_fill()
        for j in range(4):
            fd(a)
            lt(90)
        end_fill()
        pu()
        rt(90)
        fd(a)
        lt(90)
        pd()
    pu()
    rt(90)
    bk(5 * a)
    lt(90)
    fd(a)
    pd()
