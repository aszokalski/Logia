def powiel(s, n):
    ret = ""
    ns = str(n)
    for i in range(len(s)):
        ret += s[i] * int(ns[i % len(ns)])
    return ret

