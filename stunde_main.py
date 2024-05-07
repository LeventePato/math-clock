from random import randrange

stunde = 5 #randrange(1, 25)                                                         # TODO: live-Uhrzeit einfügen

hälfte_von_stunde = stunde / 2                                      # die hälfte der Uhrzeit wird bei der Multiplikation gebraucht
if stunde % 2:
    hälfte_von_stunde = int(hälfte_von_stunde) + 1

viertel_von_stunde = hälfte_von_stunde / 2
if hälfte_von_stunde % 2:
    viertel_von_stunde = int(viertel_von_stunde) + 1

erste_operatoration_für_stunde = 1 #randrange(1, 5)                    # 1=+|2=-|3=/|4=*
zweite_operatoration_für_stunde = 3 #randrange(1, 5)                  # 1=+|2=-|3=/|4=*

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


if erste_operatoration_für_stunde == 1:                     # x + y ? z
    erster_operator_für_stunde = "+"

    if zweite_operatoration_für_stunde == 1:                # x + y + z
        ergebnis_erste_rechnung = 100           # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= stunde - 1 or ergebnis_erste_rechnung < 2:        # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein +1
            erste_zahl = randrange(2, stunde - 3)                                          # TODO: stunde manchmal zu klein
            zweite_zahl = randrange(2, stunde - 3)
            ergebnis_erste_rechnung = erste_zahl + zweite_zahl
            dritte_zahl = stunde - ergebnis_erste_rechnung

    elif zweite_operatoration_für_stunde == 2:                                                # x + y - z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= stunde + 1 or ergebnis_erste_rechnung > 100:      # Bedingungen: Ergebnis größer als Uhrzeit (Std), ein-/zweistellige Zahl, kein +1/-1
            erste_zahl = randrange(2, 98)
            zweite_zahl = randrange(2, 98)
            ergebnis_erste_rechnung = erste_zahl + zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - stunde

    elif zweite_operatoration_für_stunde == 3:                                                # x + y : z
        zweite_zahl = randrange(4, 100)
        ergebnis_erste_rechnung = randrange(2, stunde - 2)
        dritte_zahl = zweite_zahl / ergebnis_erste_rechnung
        erste_zahl = stunde - ergebnis_erste_rechnung

    else:            # x + y * z
        ergebnis_erste_rechnung = 101           # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= stunde - 1 or ergebnis_erste_rechnung < 2:         # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein +1/*1, Punkt vor Strich
            zweite_zahl = randrange(2, hälfte_von_stunde)
            dritte_zahl = randrange(2, hälfte_von_stunde)
            ergebnis_erste_rechnung = zweite_zahl * dritte_zahl
            erste_zahl = stunde - ergebnis_erste_rechnung


elif erste_operatoration_für_stunde == 2:         # x - y ? z
    erster_operator_für_stunde = "-"

    if zweite_operatoration_für_stunde == 1:            # x - y + z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= stunde - 1 or ergebnis_erste_rechnung < 2:            # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), zweistellige Zahl, kein -1/+1
            erste_zahl = randrange(3, 100)
            zweite_zahl = randrange(2, erste_zahl)
            ergebnis_erste_rechnung = erste_zahl - zweite_zahl
            dritte_zahl = stunde - ergebnis_erste_rechnung

    elif zweite_operatoration_für_stunde == 2:          # x - y - z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= stunde + 1:            # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein -1, keine dreistellige Zahl
            erste_zahl = randrange(stunde + 3, 100)
            zweite_zahl = randrange(2, 98)
            ergebnis_erste_rechnung = erste_zahl - zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - stunde

    elif zweite_operatoration_für_stunde == 3:          # x - x : z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= stunde + 1 or ergebnis_erste_rechnung % stunde:         # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein -1/:1, Punkt vor Strich
            zweite_zahl = randrange(2, 100)
            dritte_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = zweite_zahl / dritte_zahl
            erste_zahl = ergebnis_erste_rechnung + stunde

    else:           # x - y * z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= stunde + 1 or ergebnis_erste_rechnung < 2:         # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein -1/*1, Punkt vor Strich
            zweite_zahl = randrange(2, 50)
            dritte_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = zweite_zahl * dritte_zahl
            erste_zahl = ergebnis_erste_rechnung + stunde

elif erste_operatoration_für_stunde == 3:           # x : y ? z
    erster_operator_für_stunde = ":"

    if zweite_operatoration_für_stunde == 1:            # x : y + z
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= stunde - 1 or erste_zahl % zweite_zahl or ergebnis_erste_rechnung < 2:           # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein :1/+1, Ergebnis soll eine ganze Zahl sein
            erste_zahl = randrange(2, 100)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl / zweite_zahl
            dritte_zahl = stunde - ergebnis_erste_rechnung

    elif zweite_operatoration_für_stunde == 2:          # x : y - z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= stunde + 1 or erste_zahl % zweite_zahl or ergebnis_erste_rechnung < 2:            # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein :1/-1, Ergebnis soll eine ganze Zahl sein
            erste_zahl = randrange(stunde * 4, 100)
            zweite_zahl = randrange(2, erste_zahl)
            ergebnis_erste_rechnung = erste_zahl / zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - stunde

    elif zweite_operatoration_für_stunde == 3:          # x : y : z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung < stunde * 2 or erste_zahl % zweite_zahl or ergebnis_erste_rechnung % stunde:            # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein :1, Ergebnis soll eine ganze Zahl sein
            if stunde == 1:
                erste_zahl = randrange(stunde * 4, 100)
                zweite_zahl = randrange(2, stunde * 2 + 1)
                ergebnis_erste_rechnung = erste_zahl / zweite_zahl
                dritte_zahl = ergebnis_erste_rechnung / stunde

            else:
                erste_zahl = randrange(stunde * 4, 100)
                zweite_zahl = randrange(2, stunde * 2)
                ergebnis_erste_rechnung = erste_zahl / zweite_zahl
                dritte_zahl = ergebnis_erste_rechnung / stunde

    else:           # x : y * z
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while ergebnis_erste_rechnung > hälfte_von_stunde or stunde % ergebnis_erste_rechnung or ergebnis_erste_rechnung < 2:          # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein :1/*1, Ergebnis soll eine ganze Zahl sein
            erste_zahl = randrange(2, 100)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl / zweite_zahl
            dritte_zahl = stunde / ergebnis_erste_rechnung

else:           # x * y ? z
    erster_operator_für_stunde = "*"

    if zweite_operatoration_für_stunde == 1:            # x * y + z
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= stunde - 1:            # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein *1/+1
            erste_zahl = randrange(2, hälfte_von_stunde + 1)        # TODO randrange manchmal lehre Menge
            zweite_zahl = randrange(2, hälfte_von_stunde + 1)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = stunde - ergebnis_erste_rechnung

    elif zweite_operatoration_für_stunde == 2:          # x * y - z
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= stunde + 1 or ergebnis_erste_rechnung > 100:           # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein *1/-1, zweistellige Zahl
            erste_zahl = randrange(2, 50)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - stunde

    elif zweite_operatoration_für_stunde == 3:
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= stunde * 2 or ergebnis_erste_rechnung > 100 or ergebnis_erste_rechnung % stunde: # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein *1/:1
            erste_zahl = randrange(2, 50)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung / stunde

    else:
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while stunde % ergebnis_erste_rechnung or ergebnis_erste_rechnung < 2:           # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein *1
            erste_zahl = randrange(2, viertel_von_stunde + 1)
            zweite_zahl = randrange(2, viertel_von_stunde + 1)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = stunde / ergebnis_erste_rechnung

aufgabe_für_stunde_ausgeben()
#print(ergebnis_erste_rechnung, zweiter_operator_für_stunde, int(dritte_zahl))
print(stunde)
#print(erste_zahl)
#print(zweite_zahl)
print(int(ergebnis_erste_rechnung))

##print(hälfte_von_stunde)
#print(viertel_von_stunde)