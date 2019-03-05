def litera(slowa):
    alfabet="abcdefghijklmnopqrstuvwxyz"
    wystepowania = {}
    for lit in alfabet:
        wystepowania[lit] = 0
    for slowo in slowa:
        uzyte = []
        for lite in slowo:
            if lite not in uzyte:
                wystepowania[lite] += slowo.count(lite)
                uzyte.append(lite)
        uzyte.clear()
    return najw(wystepowania)

def najw(dictionary):
    ret = []
    maxk = 0
    for litera in dictionary.items():
        if litera[1] > maxk:
            ret.clear()
            ret.append(litera[0])
            maxk = litera[1]
        elif litera[1] == maxk:
            ret.append(litera[0])
    ret.sort()
    return ret
