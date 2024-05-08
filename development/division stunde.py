from random import randrange
from Unittest.helpers_division import factor_division_addition

stunde = 16 #randrange(5, 24)                                                         # TODO: live-Uhrzeit einfügen

erste_operatoration_für_stunde = 3                                  # 1=+|2=-|3=/|4=*
zweite_operatoration_für_stunde = 4 #randrange(1, 5)                # 1=+|2=-|3=/|4=*

hälfte_von_stunde = stunde / 2                                      # die hälfte der Uhrzeit wird bei der Multiplikation gebraucht
if stunde % 2:
    hälfte_von_stunde = int(hälfte_von_stunde) + 1

if stunde % 2 > 0 and stunde % 3 > 0:
    zweite_operatoration_für_stunde = randrange(1, 4)          # Primzahlen können nicht das Ergebnis einer Multiplikation werden, weswegen diese ausgeschlossen wird

if stunde < 5:
    zweite_operatoration_für_stunde = randrange(2, 4)

if zweite_operatoration_für_stunde == 1:
    zweiter_operator_für_stunde = "+"
elif zweite_operatoration_für_stunde == 2:
    zweiter_operator_für_stunde = "-"
elif zweite_operatoration_für_stunde == 3:
    zweiter_operator_für_stunde = ":"
else:
    zweiter_operator_für_stunde = "*"

def aufgabe_für_stunde_ausgeben():                             # zum ausgeben auf der Konsole benötigt
    print(int(erste_zahl), erster_operator_für_stunde, int(zweite_zahl), zweiter_operator_für_stunde, int(dritte_zahl))


if erste_operatoration_für_stunde == 3:           # x : y ? z
    erster_operator_für_stunde = ":"

#stays here, implements the logic
    if zweite_operatoration_für_stunde == 1:            # x : y + z
        first_number, second_number, third_number = factor_division_addition (stunde)            

    elif zweite_operatoration_für_stunde == 2:          # x : y - z  
        ergebnis_erste_rechnung = randrange(int(stunde + 2), 49)
        dritte_zahl = ergebnis_erste_rechnung - stunde
        zweite_zahl = randrange(2, int(100 / ergebnis_erste_rechnung + 1))
        erste_zahl = ergebnis_erste_rechnung * zweite_zahl

    elif zweite_operatoration_für_stunde == 3:          # x : y : z
        ergebnis_erste_rechnung = 100
        while ergebnis_erste_rechnung > 49:
            ergebnis_erste_rechnung = stunde * randrange(2, 49)
        dritte_zahl = ergebnis_erste_rechnung / stunde
        erste_zahl = 101
        while erste_zahl > 100:
            erste_zahl = ergebnis_erste_rechnung * randrange(2, stunde * 2)
        zweite_zahl = erste_zahl / ergebnis_erste_rechnung 

    else:                                               # x : y * z
        dritte_zahl = stunde - randrange(2, int(hälfte_von_stunde))
        ergebnis_erste_rechnung = stunde / dritte_zahl
        erste_zahl = randrange(int(ergebnis_erste_rechnung * 2), 100)
        zweite_zahl = erste_zahl / ergebnis_erste_rechnung

        

                
aufgabe_für_stunde_ausgeben()
#print(ergebnis_erste_rechnung, zweiter_operator_für_stunde, int(dritte_zahl))
print(stunde)
#print(erste_zahl)
#print(zweite_zahl)
print(int(ergebnis_erste_rechnung))



