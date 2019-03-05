def maksos(x):
    osiedla = []
    osiedle = []
    for i in range(len(x)):
        osiedle.append(x[i])
        if i + 1 < len(x) and x[i + 1] - x[i] > 3:
            osiedla.append(len(osiedle))
            osiedle = []
        elif i + 1 == len(x):
            if len(osiedle) > 0:
                osiedla.append(len(osiedle))
            if x[0] <= 3:
                osiedla[0] += 1
    return max(osiedla)
