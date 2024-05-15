from random import randrange

def count_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:
            count += 1
            if i != n // i:  # Check if the divisor is not the square root of n to avoid counting it twice
                count += 1
    return count



def factor_subtraction_addition(stunde):
    ergebnis_erste_rechnung = randrange(2, stunde - 1)
    dritte_zahl = stunde - ergebnis_erste_rechnung
    erste_zahl = randrange(ergebnis_erste_rechnung + 2, 100)
    zweite_zahl = ergebnis_erste_rechnung + erste_zahl
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_subtraction_subtraction(stunde):
    ergebnis_erste_rechnung = randrange(2, stunde + 3)
    dritte_zahl = ergebnis_erste_rechnung - stunde
    erste_zahl = randrange(ergebnis_erste_rechnung + 2, 100)
    zweite_zahl = erste_zahl - ergebnis_erste_rechnung
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_subtraction_division(stunde):
    ergebnis_erste_rechnung = randrange(stunde + 2, 50)
    erste_zahl = ergebnis_erste_rechnung - stunde
    zweite_zahl = randrange((ergebnis_erste_rechnung * 2), 100)
    dritte_zahl = ergebnis_erste_rechnung * zweite_zahl
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_subtraction_multiplication(stunde):
    ergebnis_erste_rechnung = randrange(stunde + 2, 100)
    while count_factors(ergebnis_erste_rechnung) < 3:
        ergebnis_erste_rechnung = randrange(stunde + 2, 100)
    erste_zahl = ergebnis_erste_rechnung - stunde
    zweite_zahl = randrange(2, int(ergebnis_erste_rechnung / 2) + 1)
    dritte_zahl = ergebnis_erste_rechnung / zweite_zahl
    return erste_zahl, zweite_zahl, dritte_zahl
