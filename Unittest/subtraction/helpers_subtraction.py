import random


faktoren = [[] for _ in range(100)]         #erstellt einen array mit 100 lehren arrays um die Faktoren der Zahlen von 0 bis 100 zu speichern
for i in range(2, 100):                     #schaut sich die Zahlen von 2 bis 100 an, da 0 und 1 keine Teiler haben
    for j in range(2, int(i/2 + 1)):        #schaut sich die Zahlen zwischen 1 und der hälfe von i an, da jede Yahl durch 1 teilbar ist unde der größte Teiler eineR Zahl seine hälfte sein kann 
        if i % j == 0:                      #überprüft ob j ein Faktor von i ist
            faktoren[i].append(j)           # wenn ja wird j im array von i gespeichert

prime_numbers = []                          #erstellt einen lehren array der Primzahlen speichert
for i in range(2, 100):                     #schaut sich alle Zahlen zwischen 2 und 100 an, da 1 der Faktor von jeder Yahl ist und später somit endlos schleifen verursachen würde
    prime = (len(faktoren[i]) == 0)         #überprüft die Anzahl der Faktoren von i
    if prime == True:
        prime_numbers.append(i)             #wenn i keine Faktoren außer 1 und sich selber hat wird sie als Primzahl gespeichert


def factor_subtraction_addition(stunde):
    if stunde < 3:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(1, stunde - 1)
        dritte_zahl = stunde - ergebnis_erste_rechnung
        erste_zahl = random.randrange(ergebnis_erste_rechnung + 2, 100)
        zweite_zahl = erste_zahl - ergebnis_erste_rechnung
        return erste_zahl, zweite_zahl, dritte_zahl

def factor_subtraction_subtraction(stunde):
    ergebnis_erste_rechnung = random.randrange(stunde + 2, 97)
    dritte_zahl = ergebnis_erste_rechnung - stunde
    erste_zahl = random.randrange(ergebnis_erste_rechnung + 2, 100)
    zweite_zahl = erste_zahl - ergebnis_erste_rechnung
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_subtraction_division(stunde):
    ergebnis_erste_rechnung = random.randrange(stunde + 1, 50)
    erste_zahl = ergebnis_erste_rechnung + stunde
    zweite_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
    while ergebnis_erste_rechnung not in faktoren[zweite_zahl]:
        zweite_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
    dritte_zahl = zweite_zahl / ergebnis_erste_rechnung
    return erste_zahl, zweite_zahl, dritte_zahl

def factor_subtraction_multiplication(stunde):
    ergebnis_erste_rechnung = random.randrange(stunde + 2, 100)
    while ergebnis_erste_rechnung in prime_numbers:
        ergebnis_erste_rechnung = random.randrange(stunde + 2, 100)
    erste_zahl = ergebnis_erste_rechnung + stunde 
    zweite_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
    dritte_zahl = ergebnis_erste_rechnung / zweite_zahl
    return erste_zahl, zweite_zahl, dritte_zahl
