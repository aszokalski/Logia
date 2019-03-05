def ostatni(n, k):
    stol = [i for i in range(1, n + 1)]
    krzesla = stol
    
    while len(stol) < k:
        stol += stol
    index = 0
    while len(stol) > 0:
        index = (index + k - 1) % len(stol)
        ost = stol[index]
        #print(ost, stol, index)
        stol = stol[:index] + stol[index + 1:]


    return ost

