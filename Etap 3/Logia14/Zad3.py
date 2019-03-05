def spotkanie(t1, t2):
    t1 = (t1 * 100) [:100]
    t2 = (t2 * 100) [:100]

    p = [[0,0], [0,0]]
    for k1, k2, i in zip(t1, t2, range(100)):
        for act in [[k1, 0],[k2,1]]:
            if act[0] is 'g':
                p[act[1]][0] += 1
            elif act[0] is 'd':
                p[act[1]][0] -= 1
            elif act[0] is 'p':
                p[act[1]][1] += 1
            elif act[0] is 'l':
                p[act[1]][1] -= 1
        if p[0] == p[1]:
            return i + 1
    return 0
