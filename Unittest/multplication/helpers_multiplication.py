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


def teilbarkeit(n):                         #wird benötigt um zu überprüfen ob eine Multiplikation überhaupt Möglich ist
    for ergebnis_erste_rechnung in range(4, int(n / 2) + 1):
        if ergebnis_erste_rechnung in faktoren[n]:
            return True
    return False                            #überprüft ob es überhaupt Faktoren gibt (True) oder nocht (False)

def doppelte_teilbarkeit(stunde):           #wird nur bei der doppelten Multiplikation benötigt um zu überprüfen ob die Faktoren der Stunde selber Faktoren haben
    for ergebnis_erste_rechnung in range(4, int(stunde / 2) + 1):
        if ergebnis_erste_rechnung in faktoren[stunde]:
            for erste_zahl in range(2, int (ergebnis_erste_rechnung / 2) + 1):
                if erste_zahl in faktoren[ergebnis_erste_rechnung]:
                    return True
    return False                            #überprüft ob ein beliebiger Faktor überhaupt einen Faktor hat (True) oder nicht (False)


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
        while ergebnis_erste_rechnung in prime_numbers or (stunde not in faktoren[ergebnis_erste_rechnung] and stunde != 1):
            ergebnis_erste_rechnung = random.randrange(stunde * 2, 100)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = ergebnis_erste_rechnung / stunde 
        return erste_zahl, zweite_zahl, dritte_zahl

def factor_multiplication_multiplication(stunde):
    if doppelte_teilbarkeit(stunde) == False:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(4, int(stunde / 2) + 1)
        while ergebnis_erste_rechnung in prime_numbers or ergebnis_erste_rechnung not in faktoren[stunde]:
            ergebnis_erste_rechnung = random.randrange(4, int(stunde / 2) + 1)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = stunde / ergebnis_erste_rechnung
        return erste_zahl, zweite_zahl, dritte_zahl
