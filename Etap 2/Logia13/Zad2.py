def kiedy(x, y, z):
    position = 0
    days = 0
    polki = [z * i for i in range(int(1000 / z) + 1)]
    while(position < 1000):
        days += 1
        position += x
        if position >= 1000: break
        for j in range(y):
            if position in polki: break
            else: position -= 1
        
    return days
