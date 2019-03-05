def maxx(slowo):
    ret = ""
    alfabet="aąbcćdeęfghijklłmnńoóprstuwxyz"
    for litera in alfabet:
        if litera in slowo:
            lslowo = ""
            start = False
            for i in range(len(slowo)):
                if not start and slowo[i] == litera:
                    start = True
                if litera not in slowo[i:]:
                    start = False
                if start:
                    lslowo += slowo[i]
            if len(lslowo) > len(ret):
                ret = lslowo
    return ret
