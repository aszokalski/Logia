def ilez(s):
    samogloski = "aeiouy"
    
    if ilesam(s) is 0:
        return - 2
    elif ilesam(s) is 1:
        return - 1
    
    start = 0
    end = 0
    
    for i in range(len(s)):
        if s[i] in samogloski:
            start = i
            break
    for j in range(len(s))[::-1]:
        if s[j] in samogloski:
            end = j
            break
    return end - start - 1
def ilesam(s):
    samogloski = "aeiouy"
    ret = 0
    for lit in s:
        if lit in samogloski:
            ret += 1
    return ret
