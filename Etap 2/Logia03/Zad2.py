def lc(s):
    ret = ""
    for i in range(0, len(s), 2):
        ret += s[i] * int(s[i+1])
    return ret
