def dodajr(l):
    wynik = 0
    for rz in l:
        wynik += zrzymskich(rz)
    return narzymskie(wynik)


def zrzymskich(n):
    rzymskie = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
    wynik = 0
    for i in range(len(n)):
        if i + 1 < len(n) and rzymskie[n[i + 1]] > rzymskie[n[i]]:
            wynik -= rzymskie[n[i]]
        else:
            wynik += rzymskie[n[i]]
    return wynik

def narzymskie(n):
    rzymskie = {
        1 : 'I',
        5 : 'V',
        10 : 'X',
        50 : 'L',
        100 : 'C',
        500 : 'D',
        1000 : 'M'
        }
    n = str(n)
    liczba = ""
    for i in range(len(n)):
        c = n[i]
        q = ""
        if int(c) > 5 and int(c) < 9:
            c = str(int(c) - 5)
            q += rzymskie[5 * pow(10, len(n) - 1 - i)]
        if c is '4':
            q += rzymskie[1 * pow(10, len(n) - 1 - i)] + rzymskie[5 * pow(10, len(n) - 1 - i)]
        elif c is '9':
            q += rzymskie[1 * pow(10, len(n) - 1 - i)] + rzymskie[10 * pow(10, len(n) - 1 - i)]
        elif c is '5':
            q += rzymskie[5 * pow(10, len(n) - 1 - i)]
        elif c is '1' and i < len(n) - 1:
            q += rzymskie[1 * pow(10, len(n) - 1 - i)]
        else:
            for j in range(int(c)):
                q += rzymskie[1 * pow(10, len(n) - 1 - i)]
        liczba += q
    return liczba
