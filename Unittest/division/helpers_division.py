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
    for i in range(4, int(n / 2) + 1):
        if i in faktoren[n]:
            return True
    return False                            #überprüft ob es überhaupt Faktoren gibt (True) oder nocht (False)

def doppelte_teilbarkeit(n):           #wird nur bei der doppelten Multiplikation benötigt um zu überprüfen ob die Faktoren der Stunde selber Faktoren haben
    for i in range(4, int(n / 2) + 1):
        if i in faktoren[n]:
            for erste_zahl in range(2, int (i / 2) + 1):
                if erste_zahl in faktoren[i]:
                    return True
    return False                            #überprüft ob ein beliebiger Faktor überhaupt einen Faktor hat (True) oder nicht (False)


def factor_division_addition(stunde):
    if stunde < 3:
        return 1, 1, 1
    else:
        dritte_zahl = stunde - random.randrange (2,stunde - 1)
        ergebnis_erste_rechnung = stunde - dritte_zahl
        erste_zahl = ergebnis_erste_rechnung * random.randrange(2, int(100 / ergebnis_erste_rechnung))
        zweite_zahl = erste_zahl / ergebnis_erste_rechnung
        return erste_zahl, zweite_zahl, dritte_zahl

def factor_division_subtraction(stunde):
    ergebnis_erste_rechnung = random.randrange(int(stunde + 2), 49)
    dritte_zahl = ergebnis_erste_rechnung - stunde
    zweite_zahl = random.randrange(2, int(100 / ergebnis_erste_rechnung + 1))
    erste_zahl = ergebnis_erste_rechnung * zweite_zahl
    return erste_zahl, zweite_zahl, dritte_zahl


def factor_division_division(stunde):
    if stunde < 1:
        return 1, 1, 1
    else:
        ergebnis_erste_rechnung = 100
        while ergebnis_erste_rechnung > 49:
            ergebnis_erste_rechnung = stunde * random.randrange(2, 49)
        dritte_zahl = ergebnis_erste_rechnung / stunde
        erste_zahl = 101
        while erste_zahl > 100:
            erste_zahl = ergebnis_erste_rechnung * random.randrange(2, stunde * 2)
        zweite_zahl = erste_zahl / ergebnis_erste_rechnung 


        erste_zahl = random.randrange(stunde * 4, 100)
        while doppelte_teilbarkeit(erste_zahl) == False:
            erste_zahl
        return erste_zahl, zweite_zahl, dritte_zahl

def factor_division_multiplication(stunde):
    if stunde < 4:
        return 1, 1, 1
    else : 
        ergebnis_erste_rechnung = random.choice(faktoren[stunde])
        zweite_zahl = random.choice(faktoren[ergebnis_erste_rechnung])
        erste_zahl = ergebnis_erste_rechnung * zweite_zahl
        dritte_zahl = stunde / ergebnis_erste_rechnung
        return erste_zahl, zweite_zahl, dritte_zahl
