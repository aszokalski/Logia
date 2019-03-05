def pionek(slowo):
    pos = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if slowo[i * 9 + j * 3 + k] == 'c':
                    pos.append([i, j, k])
                if len(pos) == 2:
                    break
            else:
                continue
            break
        else:
            continue
        break

    ret = max(pos[0][0] - pos[1][0], pos[1][0] - pos[0][0]) + max(pos[0][1] - pos[1][1], pos[1][1] - pos[0][1]) + max(pos[0][2] - pos[1][2], pos[1][2] - pos[0][2])

    return ret

