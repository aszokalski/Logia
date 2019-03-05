
def mecz(wyniki, n):
    pkt_alka = 0
    pkt_olka = 0
    ilepartii = int(len(wyniki) / (2 * n))
    for i in range(ilepartii):
        wyn_alka = 0
        wyn_olka = 0
        for j in range(2):
            for k in range(n):
                if(j == 0):
                    wyn_alka += int(wyniki[(i * 2 * n) + (j * n) + k])
                else:
                    wyn_olka += int(wyniki[(i * 2 * n) + (j * n) + k])
                
        if(wyn_alka > wyn_olka):
            pkt_alka += 1
        elif(wyn_alka < wyn_olka):
            pkt_olka += 1
    if(pkt_alka > pkt_olka):
        return "Alek"
    elif(pkt_alka < pkt_olka):
        return "Olek"
    else:
        return "Remis"
