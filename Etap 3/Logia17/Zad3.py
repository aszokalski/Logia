najw = 0

def planeta(n, adresy):
    global najw
    najw = 0
    osiedle(adresy, n, [], [])
    ret = najw
    najw = 0
    return ret

def osiedle(adresy, n, os, proc):
    koniec = True
    global najw
    for adres in adresy:
        if len(os) is 0 or adres not in proc and liczodleglosc(os[-1], adres, n) <= 5:
            os.append(adres)
            proc.append(adres)
            koniec = False
            osiedle(adresy, n, os, proc)
    if koniec:
        najw = max(najw, len(os))
        if len(proc) < len(adresy):
            osiedle(adresy, n, [], proc)
        return
    
def liczodleglosc(a, b, n):
    return min(abs(a[0] - b[0]), min((n - a[0]) + b[0], (n - b[0]) + a[0])) + min(abs(a[1] - b[1]), min((n - a[1]) + b[1], (n - b[1]) + a[1]))
