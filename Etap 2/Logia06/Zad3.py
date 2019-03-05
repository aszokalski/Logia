def szyfr(slowo, klucz):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    slownik = generujpary()
    wyn = ""
    for i in range(0, len(slowo), 2):
        wyn += slownik[((alfabet.index(slowo[i]) * 26) + alfabet.index(slowo[i + 1]) + klucz) % 676]
    return wyn

def generujpary():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    slownik = {}
    for literap in alfabet:
        for literaq in alfabet:
            slownik[((alfabet.index(literap) * 26) + alfabet.index(literaq))] = literap + literaq
    return slownik
