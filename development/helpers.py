# start refactoring this into a function

def factor_division_addition():
    dritte_zahl = stunde - randrange (2,stunde -2)
    ergebnis_erste_rechnung = stunde - dritte_zahl
    erste_zahl = ergebnis_erste_rechnung * randrange(2, int(100 / ergebnis_erste_rechnung))
    zweite_zahl = erste_zahl / ergebnis_erste_rechnung
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_division_addition():
    ergebnis_erste_rechnung = randrange(int(stunde + 2), 49)
    dritte_zahl = ergebnis_erste_rechnung - stunde
    zweite_zahl = randrange(2, int(100 / ergebnis_erste_rechnung + 1))
    erste_zahl = ergebnis_erste_rechnung * zweite_zahl

def factor_division_division():
    ergebnis_erste_rechnung = 100
    while ergebnis_erste_rechnung > 49:
        ergebnis_erste_rechnung = stunde * randrange(2, 49)
    dritte_zahl = ergebnis_erste_rechnung / stunde
    erste_zahl = 101
    while erste_zahl > 100:
        erste_zahl = ergebnis_erste_rechnung * randrange(2, stunde * 2)
    zweite_zahl = erste_zahl / ergebnis_erste_rechnung 

def factor_division_multiplication():
    dritte_zahl = stunde  randrange(2, hälfte_von_stunde)
    ergebnis_erste_rechnung = stunde / dritte_zahl
    erste_zahl = randrange(int(ergebnis_erste_rechnung * 2), 100)
    zweite_zahl = erste_zahl / ergebnis_erste_rechnung