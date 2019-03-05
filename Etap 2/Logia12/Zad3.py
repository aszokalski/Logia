def miasta(a, b,c):
    res = [""] * (3 * len(a))
    result = ""
    for elem in a:
        res[a.find(elem) + b.find(elem) + c.find(elem)] += elem
    for char in res:
        if char:
            result += char
    return(result)
        
