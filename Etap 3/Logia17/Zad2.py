def abc(slowo):
    kolejnosc = "ncz"
    grupy = [[]]

    #dzielimy słowo na grupy takich samych liter z pominięciem liter nieistotnych
    for l in slowo:
        if l not in kolejnosc:
            continue
        if not grupy[-1] or grupy[-1][-1] == l:
            grupy[-1].append(l)
        else:
            grupy.append([l])

    #tworzymy listy przechowujące dane o długości danej grupy i kolejności jej litery w słowie "ncz"
    kol = []
    dlug = []

    wynik = 0
    for i in range(len(grupy)):
        grupa = grupy[i]
        kol.append(kolejnosc.index(grupa[0]))
        dlug.append(len(grupa))

        if i > 0:
            j = i - 1
            #Szukamy poprzedniej grupy wykluczjąc grupy puste
            while not kol[j]:
                j -= 1
            #Jeśli poprzednia grupa ma większą kolejność (składa się z liter występujących pózniej w słowie "ncz")
            if kol[j] > kol[i]:
                #Porównujemy długości obecnej i poprzedniej grupy. Jeśli grupa poprzednia jest mniejsza lub równa - usuwamy ją,
                #a jeśli obecna jest mniejsza - usuwamy obecną.
                if dlug[j] <= dlug[i]:
                    grupy[j] = []
                    wynik += dlug[j]
                else:
                    grupy[i] = []
                    wynik += dlug[i]
    
    return wynik

        
                
