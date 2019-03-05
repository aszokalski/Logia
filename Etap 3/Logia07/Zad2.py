def liczpal(liczby):
    wynik = []
    for liczba in liczby:
        n = liczba
        dodawania = 0
        while(czypal(str(n)) is not True):
            odw = int(str(n)[::-1])
            n += odw
            dodawania += 1
        wynik.append([n, dodawania])
    return wynik
def czypal(s):
    if s == s[::-1]:
        return True
    return False
