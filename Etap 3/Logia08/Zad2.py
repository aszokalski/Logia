def dt(trasa):
    odleglosc = dict()
    
    odleglosc['Tenerife'] = dict()
    odleglosc['Tenerife']['La Gomera'] = 28
    odleglosc['Tenerife']['La Palma'] = 85
    odleglosc['Tenerife']['El Hierro'] = 88

    odleglosc['La Gomera'] = dict()
    odleglosc['La Gomera']['Tenerife'] = 28
    odleglosc['La Gomera']['La Palma'] = 58
    odleglosc['La Gomera']['El Hierro'] = 61

    odleglosc['La Palma'] = dict()
    odleglosc['La Palma']['Tenerife'] = 85
    odleglosc['La Palma']['La Gomera'] = 58
    odleglosc['La Palma']['El Hierro'] = 68

    odleglosc['El Hierro'] = dict()
    odleglosc['El Hierro']['Tenerife'] = 88
    odleglosc['El Hierro']['La Gomera'] = 61
    odleglosc['El Hierro']['La Palma'] = 68

    wynik = 0
    for i in range(1, len(trasa)):
        wynik += odleglosc[trasa[i-1]][trasa[i]]

    return wynik
