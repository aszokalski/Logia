def szyfr(s, klucz1, klucz2):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    samogloski = "aeiouy"
    ret = ""
    for lit in s:
        if lit in samogloski:
            kl = klucz1
        else:
            kl = klucz2
        ret += alfabet[(alfabet.index(lit) + kl) % len(alfabet)]
    return ret
