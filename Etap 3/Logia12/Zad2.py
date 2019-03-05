def pole(n, ruchy):
    odwiedzone =[ruchy[0]]
    pozycja = ruchy[0][:]
    #print("Pozycja: ", pozycja, "   Odwiedzone: ", odwiedzone)
    for npos in ruchy[1:]:
        
        while pozycja != npos:
            
            if pozycja[0] < npos[0]:
                pozycja[0] += 1
            elif pozycja[0] > npos[0]:
                pozycja[0] -= 1
                
            if pozycja[1] < npos[1]:
                pozycja[1] += 1
            elif pozycja[1] > npos[1]:
                pozycja[1] -= 1
            #print("Pozycja: ", pozycja, "   Odwiedzone: ", odwiedzone)
            if pozycja in odwiedzone:
                return pozycja
            else:
                odwiedzone.append(pozycja[:])
    return 0
