import random


faktoren = [[] for _ in range(100)]

for i in range(2, 100):
    for j in range(2, int(i/2 + 1)):
        if i % j == 0:
            faktoren[i].append(j)


prime_numbers = []

for i in range(2, 100):
    prime = (len(faktoren[i]) == 0)
    if prime == True:
        prime_numbers.append(i)

number = random.randrange(2, 100)
while number in prime_numbers:
    number = random.randrange(2, 100)
random_factor = random.choice(faktoren[number])

def teilbarkeit(stunde):
    for ergebnis_erste_rechnung in range(4, int(stunde / 2) + 1):
        if ergebnis_erste_rechnung in faktoren[stunde]:
            return True
    return False


def factor_multiplication_addition(stunde):
    if stunde < 6:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(4, stunde - 1)
        while ergebnis_erste_rechnung in prime_numbers:
            ergebnis_erste_rechnung = random.randrange(4, stunde - 1)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = stunde - ergebnis_erste_rechnung
        return erste_zahl, zweite_zahl, dritte_zahl

def factor_multiplication_subtraction(stunde):
    ergebnis_erste_rechnung = random.randrange(stunde + 2, 100)
    while ergebnis_erste_rechnung in prime_numbers:
        ergebnis_erste_rechnung = random.randrange(stunde + 2, 100)
    erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
    zweite_zahl = ergebnis_erste_rechnung / erste_zahl
    dritte_zahl = ergebnis_erste_rechnung - stunde
    return erste_zahl, zweite_zahl, dritte_zahl


def factor_multiplication_division(stunde):
    if stunde == 0:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(stunde * 2, 100)
        while ergebnis_erste_rechnung in prime_numbers or stunde not in faktoren[ergebnis_erste_rechnung]:
            ergebnis_erste_rechnung = random.randrange(stunde * 2, 100)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = ergebnis_erste_rechnung / stunde 
        return erste_zahl, zweite_zahl, dritte_zahl

def factor_multiplication_multiplication(stunde):
    if teilbarkeit(stunde) == False or stunde < 8 or stunde in prime_numbers:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(4, int(stunde / 2) + 1)
        while ergebnis_erste_rechnung in prime_numbers or ergebnis_erste_rechnung not in faktoren[stunde]:
            ergebnis_erste_rechnung = random.randrange(4, int(stunde / 2) + 1)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = stunde / ergebnis_erste_rechnung
        return erste_zahl, zweite_zahl, dritte_zahl
