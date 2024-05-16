from random import randrange

def count_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:
            count += 1
            if i != n // i:  # Check if the divisor is not the square root of n to avoid counting it twice
                count += 1
    return count

def factor_multiplication_addition(stunde):
    erste_zahl = randrange(2, int(stunde / 2))
    ergebnis_erste_rechnung = stunde
    while ergebnis_erste_rechnung > stunde - 1:
        zweite_zahl = randrange(2, int(ergebnis_erste_rechnung / erste_zahl) + 1)
        ergebnis_erste_rechnung = erste_zahl * zweite_zahl
    dritte_zahl = stunde - ergebnis_erste_rechnung
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_multiplication_subtraction(stunde):
    erste_zahl = randrange(2, 50)
    ergebnis_erste_rechnung = stunde
    while ergebnis_erste_rechnung <  stunde + 1:
        zweite_zahl = randrange(2, 50)
        ergebnis_erste_rechnung = erste_zahl * zweite_zahl
    dritte_zahl = ergebnis_erste_rechnung - stunde
    return erste_zahl, zweite_zahl, dritte_zahl


#def factor_multiplication_division(stunde):
 #   dritte_zahl = randrange(2, 50)
  #  ergebnis_erste_rechnung = randrange(2, )

#def factor_multiplication_multiplication(stunde):

