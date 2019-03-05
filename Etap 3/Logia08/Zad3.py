def szyfr(klucz, zdanie):
    alfabet = alf(klucz)
    allac = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for slowo in zdanie:
        for litera in slowo:
            ciphertext += alfabet[allac.index(litera)]
    return ciphertext

def alf(slowo):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    slowo = niepowt(slowo)
    return niepowt(slowo+alfabet)

def niepowt(slowo):
    ret = ""
    for litera in slowo:
        if litera not in ret:
            ret += litera
    return ret
