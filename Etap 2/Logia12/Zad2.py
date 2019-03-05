def convert(x, base):
    if x == 0: return 0
    pattern = "0123456789ABCDEF"
    result =""
    while x is not 0:
        result += pattern[int(x % base)]
        x = int(x / base)
    return result[::-1]
        
def ilecyfr(liczba, podstawa):
    return len(convert(liczba, podstawa))
