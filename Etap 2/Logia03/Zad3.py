def kod(s):
    samogloski = "aeiouy"
    ns=""
    curr = ""
    for i in range(len(s)):
        if s[i] not in samogloski:
            curr += s[i]
        if s[i] in samogloski:
            if curr is not "":
                if len(curr) > 1:
                    ns += curr[0] + curr[-1]
                else:
                    ns += curr
            curr = ""
            ns += s[i]
            if i is not 0 and i is not len(s) - 1:
                ns += s[i]
    if curr is not "":
        if len(curr) > 1:
            ns += curr[0] + curr[-1]
        else:
            ns += curr
    return ns

