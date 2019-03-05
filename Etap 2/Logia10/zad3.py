def robot(trasa):
    positions = []
    x = 0
    y = 0
    positions.append([x, y])
    repeated = 0
    for move in trasa:
        if move == 'N':
            x += 1
        elif move == 'S':
            x -= 1
        elif move == 'W':
            y -= 1
        elif move == 'E':
            y += 1
        if [x, y] in positions:
            repeated += 1
        positions.append([x, y])
    return repeated
        
