from random import randrange

# naive implementation of number of factors 

def count_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:
            count += 1
            if i != n // i:  # Check if the divisor is not the square root of n to avoid counting it twice
                count += 1
    return count

def factor_division_addition(stunde):
    dritte_zahl = stunde - randrange (2,stunde -2)
    ergebnis_erste_rechnung = stunde - dritte_zahl
    erste_zahl = ergebnis_erste_rechnung * randrange(2, int(100 / ergebnis_erste_rechnung))
    zweite_zahl = erste_zahl / ergebnis_erste_rechnung
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_division_subtraction(stunde):
    ergebnis_erste_rechnung = randrange(int(stunde + 2), 49)
    dritte_zahl = ergebnis_erste_rechnung - stunde
    zweite_zahl = randrange(2, int(100 / ergebnis_erste_rechnung + 1))
    erste_zahl = ergebnis_erste_rechnung * zweite_zahl
    return erste_zahl, zweite_zahl, dritte_zahl


def factor_division_division(stunde):
    ergebnis_erste_rechnung = 100
    while ergebnis_erste_rechnung > 49:
        ergebnis_erste_rechnung = stunde * randrange(2, 49)
    dritte_zahl = ergebnis_erste_rechnung / stunde
    erste_zahl = 101
    while erste_zahl > 100:
        erste_zahl = ergebnis_erste_rechnung * randrange(2, stunde * 2)
    zweite_zahl = erste_zahl / ergebnis_erste_rechnung 
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_division_multiplication(stunde):
    hälfte_von_stunde = stunde / 2
    if hälfte_von_stunde % 1 > 0:
        hälfte_von_stunde = int(stunde / 2) + 1
    ergebnis_erste_rechnung = randrange(2, hälfte_von_stunde)
    dritte_zahl = stunde / ergebnis_erste_rechnung
    zweite_zahl = randrange(2, int(ergebnis_erste_rechnung / 2) + 1)
    erste_zahl = ergebnis_erste_rechnung * zweite_zahl
    return erste_zahl, zweite_zahl, dritte_zahl

