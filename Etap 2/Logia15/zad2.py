def redukcja(x):
    x = str(x)[::-1]
    while(len(x) >= 2):
        xb = x
        for i in range(len(x) - 1):
            if i < len(x) - 1 and x[i] == x[i + 1]:
                number = str(int(x[i]) + int(x[i + 1]))
                if len(number) > 1:
                    number = number[1]
                x = x[:i] + number + x[i + 2:]
        if xb == x:
            break
    return int(x[::-1])
        
