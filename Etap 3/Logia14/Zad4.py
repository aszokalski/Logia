def ilesam(wyroby, samochody):
    wyn = 0
    for samochod in samochody:
        zapakowano = 0
        
        while zapakowano < samochod:
            if len(wyroby) == 0:
                return wyn + 1
            if zapakowano + wyroby[0][1] > samochod:
                break
            
            maks = 0
            
            for i in range(1, wyroby[0][0] + 1):
                if zapakowano + i * wyroby[0][1] <= samochod:
                    maks = i
            zapakowano += maks * wyroby[0][1]
            
            wyroby[0][0] -= maks
            if wyroby[0][0] == 0:
                wyroby = wyroby[1:]

        wyn += 1
        samochody.append(samochod)
        
        
