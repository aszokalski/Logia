def ilerazy(n, l):
    ile = 0
    ret = 0
    for i in range(len(l)):
        if i % 2 is 0:
            for j in range(l[i]):
                ile += 1
                if ile is n:
                    ret += 1
        else:
            for k in range(l[i]):
                ile -= 1
                if ile is n:
                    ret += 1
    return ret
