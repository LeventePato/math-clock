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

def teilbarkeit(n):                         #wird nur bei der doppelten Multiplikation benötigt um zu überprüfen ob die Faktoren der Stunde selber Faktoren haben
    for i in range(4, int(n / 2) + 1):
        if j in faktoren[n]:
            for erste_zahl in range(2, int (i / 2) + 1):
                if erste_zahl in faktoren[i]:
                    return True
    return False                            #überprüft ob ein beliebiger Faktor überhaupt einen Faktor hat (True) oder nicht (False)

# addition

def factor_addition_addition(minute):
    if minute < 6:
        return 1, 1, 1
    else:
        ergebnis_erste_rechnung = random.randrange(4, minute - 1)
        dritte_zahl = minute - ergebnis_erste_rechnung
        erste_zahl = random.randrange(2, ergebnis_erste_rechnung - 1)
        zweite_zahl = ergebnis_erste_rechnung - erste_zahl
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_addition_subtraction(minute):
    if minute > 4:
        ergebnis_erste_rechnung = random.randrange(minute + 2, 100)
    else:
        ergebnis_erste_rechnung = random.randrange(4, 100)
    dritte_zahl = ergebnis_erste_rechnung - minute
    erste_zahl = random.randrange(2, ergebnis_erste_rechnung - 1)
    zweite_zahl = ergebnis_erste_rechnung - erste_zahl
    return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_addition_division(minute):
    if minute < 4:
        return 1, 1, 1
    else:
        ergebnis_erste_rechnung = random.randrange(2, minute - 1)
        erste_zahl = minute - ergebnis_erste_rechnung
        zweite_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
        while ergebnis_erste_rechnung not in faktoren[zweite_zahl]:
            zweite_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
        dritte_zahl = zweite_zahl / ergebnis_erste_rechnung
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_addition_multiplication(minute):
    if minute < 6:
        return 1, 1, 1
    else : 
        ergebnis_erste_rechnung = random.randrange(4, minute - 1)
        while len(faktoren[ergebnis_erste_rechnung]) == 0:
            ergebnis_erste_rechnung = random.randrange(4, minute - 1)
        erste_zahl = minute - ergebnis_erste_rechnung 
        zweite_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        dritte_zahl = ergebnis_erste_rechnung / zweite_zahl
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)
    
# subtraktion

def factor_subtraction_addition(minute):
    if minute < 3:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(1, minute - 1)
        dritte_zahl = minute - ergebnis_erste_rechnung
        erste_zahl = random.randrange(ergebnis_erste_rechnung + 2, 100)
        zweite_zahl = erste_zahl - ergebnis_erste_rechnung
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_subtraction_subtraction(minute):
    ergebnis_erste_rechnung = random.randrange(minute + 2, 97)
    dritte_zahl = ergebnis_erste_rechnung - minute
    erste_zahl = random.randrange(ergebnis_erste_rechnung + 2, 100)
    zweite_zahl = erste_zahl - ergebnis_erste_rechnung
    return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_subtraction_division(minute):
    ergebnis_erste_rechnung = random.randrange(minute + 1, 50)
    erste_zahl = ergebnis_erste_rechnung + minute
    zweite_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
    while ergebnis_erste_rechnung not in faktoren[zweite_zahl]:
        zweite_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
    dritte_zahl = zweite_zahl / ergebnis_erste_rechnung
    return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_subtraction_multiplication(minute):
    ergebnis_erste_rechnung = random.randrange(minute + 2, 100)
    while ergebnis_erste_rechnung in prime_numbers:
        ergebnis_erste_rechnung = random.randrange(minute + 2, 100)
    erste_zahl = ergebnis_erste_rechnung + minute 
    zweite_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
    dritte_zahl = ergebnis_erste_rechnung / zweite_zahl
    return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

# division

def factor_division_addition(minute):
    if minute < 4:
        return 1, 1, 1
    else:
        ergebnis_erste_rechnung = random.randrange(2, minute - 1)
        erste_zahl = random.randrange(minute * 2 + 2, 100)
        while ergebnis_erste_rechnung not in faktoren[erste_zahl]:
            erste_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
        zweite_zahl = erste_zahl / ergebnis_erste_rechnung
        dritte_zahl = minute - ergebnis_erste_rechnung
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)
    
def factor_division_subtraction(minute):
    ergebnis_erste_rechnung = random.randrange(int(minute + 2), 49)
    dritte_zahl = ergebnis_erste_rechnung - minute
    zweite_zahl = random.randrange(2, int(100 / ergebnis_erste_rechnung + 1))
    erste_zahl = ergebnis_erste_rechnung * zweite_zahl
    return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_division_division(minute):
    if minute < 1:
        return 1, 1, 1
    else:
        ergebnis_erste_rechnung = random.randrange(minute * 2, 50)
        while minute not in faktoren[ergebnis_erste_rechnung] and minute != 1:
            ergebnis_erste_rechnung = random.randrange(minute * 2, 50)
        erste_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
        while ergebnis_erste_rechnung not in faktoren[erste_zahl]:
            erste_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
        zweite_zahl = erste_zahl / ergebnis_erste_rechnung
        dritte_zahl = ergebnis_erste_rechnung / minute
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_division_multiplication(minute):
    if minute < 4 or minute in prime_numbers:
        return 1, 1, 1
    else : 
        ergebnis_erste_rechnung = random.choice(faktoren[minute])
        erste_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
        while ergebnis_erste_rechnung not in faktoren[erste_zahl]:
            erste_zahl = random.randrange(ergebnis_erste_rechnung * 2, 100)
        zweite_zahl = erste_zahl / ergebnis_erste_rechnung
        dritte_zahl = minute / ergebnis_erste_rechnung
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)
    
# multiplikation

def factor_multiplication_addition(minute): 
    if minute < 6:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(4, minute - 1)
        while ergebnis_erste_rechnung in prime_numbers:
            ergebnis_erste_rechnung = random.randrange(4, minute - 1)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = minute - ergebnis_erste_rechnung
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_multiplication_subtraction(minute):
    ergebnis_erste_rechnung = random.randrange(minute + 2, 100)
    while ergebnis_erste_rechnung in prime_numbers:
        ergebnis_erste_rechnung = random.randrange(minute + 2, 100)
    erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
    zweite_zahl = ergebnis_erste_rechnung / erste_zahl
    dritte_zahl = ergebnis_erste_rechnung - minute
    return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)


def factor_multiplication_division(minute):
    if minute == 0:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(minute * 2, 100)
        while ergebnis_erste_rechnung in prime_numbers or (minute not in faktoren[ergebnis_erste_rechnung] and minute != 1):
            ergebnis_erste_rechnung = random.randrange(minute * 2, 100)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = ergebnis_erste_rechnung / minute 
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)

def factor_multiplication_multiplication(minute):
    if teilbarkeit(minute) == False:
        return 1, 1, 1
    else: 
        ergebnis_erste_rechnung = random.randrange(4, int(minute / 2) + 1)
        while ergebnis_erste_rechnung in prime_numbers or ergebnis_erste_rechnung not in faktoren[minute]:
            ergebnis_erste_rechnung = random.randrange(4, int(minute / 2) + 1)
        erste_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        zweite_zahl = ergebnis_erste_rechnung / erste_zahl
        dritte_zahl = minute / ergebnis_erste_rechnung
        return int(erste_zahl), int(zweite_zahl), int(dritte_zahl)


def aufgabe_für_minute(erster_operaror_für_minute, zweiter_operator_für_minute, erste_zahl, zweite_zahl, dritte_zahl):
    erste_aufgabe = erste_zahl + erster_operaror_für_minute + zweite_zahl
    gesamte_aufgabe = erste_aufgabe + zweiter_operator_für_minute + dritte_zahl
    print(gesamte_aufgabe)
    return gesamte_aufgabe
