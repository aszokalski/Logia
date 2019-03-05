def poler(s):
    total = [0,0,0,0] ##u,d,l,r
    up = 0
    down = 0
    left = 0
    right = 0
    for com in s:
        if com == 'g':
            up += 1
            down -= 1
            if up > total[0]: total[0] = up
        elif com == 'd':
            down += 1
            up -= 1
            if down > total[1]: total[1] = down
        elif com == 'l':
            left += 1
            right -= 1
            if left > total[2]: total[2] = left
        elif com == 'p':
            right += 1
            left -= 1
            if right > total[3]: total[3] = right
    return (total[0] + total[1]) * (total[2] + total[3])
