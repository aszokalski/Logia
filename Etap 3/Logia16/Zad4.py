def lnp(n, w, k):
    pola = n * n
    plansza = [[1] * (n+2)] + [[1] + [0] *n + [1] for i in range(n)] + [[1] * (n + 2)]
    zakr = False
    zwrot = 0

    
    while True:
        pw = w
        pk = k
        plansza[w][k] = 1
 #       for wi in plansza:
 #           print(wi)
 #       print("")
 #       print("")
        if zwrot is 0:
            k += 1
        elif zwrot is 1:
            w += 1
        elif zwrot is 2:
            k -= 1
        elif zwrot is 3:
            w -= 1

            
        if plansza[w][k] is 1:
            if zakr is True:
                break
            w = pw
            k = pk
            zwrot = (zwrot + 1) % 4
            zakr = True
            continue
        zakr = False

    ile = 0
    for wiersz in plansza:
        ile += wiersz.count(0)
    return ile
            
        
        
