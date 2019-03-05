def spr(s):
    dlug = [0]
    count = False
    k = 0
    j = 0
    a = 0
    for i in range(len(s)):
        if s[i] is "a":
            a += 1
            if a > 1:
                if ile(s[j: i], "b") is not 1:
                    dlug[k] = 0
                dlug.append(0)
                k += 1
            j = i
            count = True
        if count:
            dlug[k] += 1
        if i is len(s) - 1:
            if ile(s[j: i], "b") is not 1:
                    dlug[k] = 0
    return max(dlug)
                
def ile(s, x):
    ile = 0
    for lit in s:
        if lit is x:
            ile += 1
    return ile
