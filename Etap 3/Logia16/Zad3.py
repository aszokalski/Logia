def maxu(lista):
    sekundy = [0]
    for u in lista:
        start = u[0]
        kon = start + u[1]
        while len(sekundy) - 1 < kon:
            sekundy.append(0)
        for i in range(start, kon + 1):
            sekundy[i] += 1
    return max(sekundy)
