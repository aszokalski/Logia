def sumas(s1, s2):
    alfabet = "abcdefghij"
    a = 0
    b = 0
    for i in range(len(s1)):
        a += (alfabet.index(s1[i]) * pow(10, i))
    for j in range(len(s2)):
        b += (alfabet.index(s2[j]) * pow(10, j))
    wyn = str(a + b)
    ret = ""
    for elem in wyn:
        ret += alfabet[int(elem)]
    return ret
