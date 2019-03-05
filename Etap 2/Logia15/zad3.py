def ile2(x, y):
    ilosc = 0
    if x == 1:
        return 1
    for i in range(1, x):
        ilosc += x * pow(9, i)
    print(ilosc)
    ilosc -= (2 * (x - 2) * 9 + 1)
    return ilosc + 1
        
        
def ile(x, y):
    if y is 0:
        return 9*pow(10,x - 1) - 9*pow(9,x - 1)
    return 9*pow(10,x - 1) - 8*pow(9,x - 1)
