def droga(lista):
    res = 0
    level = 0
    for elem in lista:
        if type(elem) is list:
            res += max(level - elem[1], elem[1] - level) + elem[0]
            level = elem[1]
        else:
            res += level + elem
            level = 0
    res += level
    return res
