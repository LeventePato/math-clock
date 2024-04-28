from random import randrange

minute = randrange(1, 60)                                                         # TODO: live-Uhrzeit einfügen

hälfte_von_minute = minute / 2                                      # die hälfte der Uhrzeit wird bei der Multiplikation gebraucht
if minute % 2:
    hälfte_von_minute = minute / 2 + 0.5

viertel_von_minute = hälfte_von_minute / 2
if hälfte_von_minute % 2:
    viertel_von_minute = hälfte_von_minute / 2 + 0.5

erste_operatoration_für_minute = 1#randrange(1, 5)                    # 1=+|2=-|3=/|4=*
zweite_operatoration_für_minute = 3#randrange(1, 5)                  # 1=+|2=-|3=/|4=*


while zweite_operatoration_für_minute == 3 and minute > 49:
    zweite_operatoration_für_minute == randrange(1, 5)              #TODO: manchmal endlosschleife


if zweite_operatoration_für_minute == 1:
    zweiter_operator_für_minute = "+"
elif zweite_operatoration_für_minute == 2:
    zweiter_operator_für_minute = "-"
elif zweite_operatoration_für_minute == 3:
    zweiter_operator_für_minute = ":"
else:
    zweiter_operator_für_minute = "*"

def aufgabe_für_minute_ausgeben():                             # zum ausgeben auf der Konsole benötigt
    print(int(erste_zahl), erster_operator_für_minute, int(zweite_zahl), zweiter_operator_für_minute, int(dritte_zahl))

if erste_operatoration_für_minute == 1:                     # x + y ? z
    erster_operator_für_minute = "+"

    if zweite_operatoration_für_minute == 1:                        # x + y + z (funktionstüchtig)
        ergebnis_erste_rechnung = 100                               # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= minute - 1 or ergebnis_erste_rechnung < 2:         # Bedingungen: Ergebnis kleiner als Uhrzeit (Min), kein +1
            erste_zahl = randrange(2, minute - 3)                                           # minute - 3 wegen der dritten Zahl
            zweite_zahl = randrange(2, minute - 3)
            ergebnis_erste_rechnung = erste_zahl + zweite_zahl
            dritte_zahl = minute - ergebnis_erste_rechnung

    elif zweite_operatoration_für_minute == 2:                      # x + y - z(funktionstüchtig)
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= minute + 1 or ergebnis_erste_rechnung > 100:      # Bedingungen: Ergebnis größer als Uhrzeit (Min), ein-/zweistellige Zahl, kein +1/-1
            erste_zahl = randrange(2, 98)
            zweite_zahl = randrange(2, 98)
            ergebnis_erste_rechnung = erste_zahl + zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - minute

    elif zweite_operatoration_für_minute == 3:                  # x + y : z TODO: manchmal endlosschleife
        ergebnis_erste_rechnung = 100
        while ergebnis_erste_rechnung >= minute - 1 or zweite_zahl % dritte_zahl > 0 or ergebnis_erste_rechnung < 2:       # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), Punkt vor Strich, kein +1/:1
            zweite_zahl = randrange(2, 100)
            dritte_zahl = randrange(2, int(zweite_zahl / 2))
            ergebnis_erste_rechnung = zweite_zahl / dritte_zahl
            erste_zahl = minute - ergebnis_erste_rechnung

    else:            # x + y * z TODO: manchmal endloschleife. wahrscheinlich wegen minute zu klein
        ergebnis_erste_rechnung = 101           # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= minute - 1 or ergebnis_erste_rechnung < 2:         # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein +1/*1, Punkt vor Strich
            zweite_zahl = randrange(2, hälfte_von_minute)
            dritte_zahl = randrange(2, hälfte_von_minute)
            ergebnis_erste_rechnung = zweite_zahl * dritte_zahl
            erste_zahl = minute - ergebnis_erste_rechnung


elif erste_operatoration_für_minute == 2:         # x - y ? z
    erster_operator_für_minute = "-"

    if zweite_operatoration_für_minute == 1:            # x - y + z TODO: manchmal endlosschleife.
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= minute - 1 or ergebnis_erste_rechnung < 2:            # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), zweistellige Zahl, kein -1/+1
            erste_zahl = randrange(3, 100)
            zweite_zahl = randrange(2, erste_zahl)
            ergebnis_erste_rechnung = erste_zahl - zweite_zahl
            dritte_zahl = minute - ergebnis_erste_rechnung

    elif zweite_operatoration_für_minute == 2:          # x - y - z (funtionstüchtig)
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= minute + 1:            # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein -1, keine dreistellige Zahl
            erste_zahl = randrange(minute + 3, 100)
            zweite_zahl = randrange(2, 98)
            ergebnis_erste_rechnung = erste_zahl - zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - minute

    elif zweite_operatoration_für_minute == 3:          # x - x : z TODO: häufig endlosschleife
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= minute + 1 or ergebnis_erste_rechnung % minute:         # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein -1/:1, Punkt vor Strich
            zweite_zahl = randrange(minute * 2 + 2, 100)
            dritte_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = zweite_zahl / dritte_zahl
            erste_zahl = ergebnis_erste_rechnung - minute

    else:           # x - y * z TODO: manchmal endlosschleife
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= minute + 1 or ergebnis_erste_rechnung < 2 or erste_zahl > 99:         # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein -1/*1, Punkt vor Strich
            zweite_zahl = randrange(2, 50)
            dritte_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = zweite_zahl * dritte_zahl
            erste_zahl = ergebnis_erste_rechnung + minute

elif erste_operatoration_für_minute == 3:           # x : y ? z
    erster_operator_für_minute = ":"

    if zweite_operatoration_für_minute == 1:            # x : y + z TODO: manchmal endlosscheife
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= minute - 1 or erste_zahl % zweite_zahl or ergebnis_erste_rechnung < 2:           # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein :1/+1, Ergebnis soll eine ganze Zahl sein
            erste_zahl = randrange(2, 100)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl / zweite_zahl
            dritte_zahl = minute - ergebnis_erste_rechnung

    elif zweite_operatoration_für_minute == 2:          # x : y - z TODO: code fehler (randrange)
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= minute + 1 or erste_zahl % zweite_zahl or ergebnis_erste_rechnung < 2:            # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein :1/-1, Ergebnis soll eine ganze Zahl sein
            erste_zahl = randrange(minute * 4, 100)
            zweite_zahl = randrange(2, erste_zahl)
            ergebnis_erste_rechnung = erste_zahl / zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - minute

    elif zweite_operatoration_für_minute == 3:          # x : y : z TODO: code fehler (randrange)
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung < minute * 2 or erste_zahl % zweite_zahl or ergebnis_erste_rechnung % stunde:            # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein :1, Ergebnis soll eine ganze Zahl sein
            if minute == 1:
                erste_zahl = randrange(minute * 4, 100)
                zweite_zahl = randrange(2, minute * 2 + 1)
                ergebnis_erste_rechnung = erste_zahl / zweite_zahl
                dritte_zahl = ergebnis_erste_rechnung / minute

            else:
                erste_zahl = randrange(minute * 4, 100)
                zweite_zahl = randrange(2, stunde * 2)
                ergebnis_erste_rechnung = erste_zahl / zweite_zahl
                dritte_zahl = ergebnis_erste_rechnung / minute

    else:           # x : y * z TODO: manchmal ungerade zahl durch gerade zahl
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while ergebnis_erste_rechnung > hälfte_von_minute or minute % ergebnis_erste_rechnung or ergebnis_erste_rechnung < 2 or erste_zahl == zweite_zahl:          # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein :1/*1, Ergebnis soll eine ganze Zahl sein
            erste_zahl = randrange(2, 100)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl / zweite_zahl
            dritte_zahl = minute / ergebnis_erste_rechnung

else:           # x * y ? z
    erster_operator_für_minute = "*"

    if zweite_operatoration_für_minute == 1:            # x * y + z TODO: code fehler (randrange). wahrschenlich minute zu klein
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while ergebnis_erste_rechnung >= minute - 1:            # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein *1/+1
            erste_zahl = randrange(2, hälfte_von_minute)
            zweite_zahl = randrange(2, hälfte_von_minute)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = minute - ergebnis_erste_rechnung

    elif zweite_operatoration_für_minute == 2:          # x * y - z (funtionsfähig)
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= minute + 1 or ergebnis_erste_rechnung > 100:           # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein *1/-1, zweistellige Zahl
            erste_zahl = randrange(2, 50)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung - minute

    elif zweite_operatoration_für_minute == 3:          # x * y / z TODO: manchmal endlosschleife wegen Zeile 18
        ergebnis_erste_rechnung = 0         # für while-Schleife benötigt
        while ergebnis_erste_rechnung <= minute * 2 or ergebnis_erste_rechnung > 100 or ergebnis_erste_rechnung % minute: # Bedingungen: Ergebnis größer als Uhrzeit (Std), kein *1/:1
            erste_zahl = randrange(2, 50)
            zweite_zahl = randrange(2, 50)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = ergebnis_erste_rechnung / minute

    else:                   # x * y * z TODO: manchmal endlosschleife; code fehler (randrange)
        ergebnis_erste_rechnung = 100         # für while-Schleife benötigt
        while minute % ergebnis_erste_rechnung or ergebnis_erste_rechnung < 2:           # Bedingungen: Ergebnis kleiner als Uhrzeit (Std), kein *1
            erste_zahl = randrange(2, viertel_von_minute + 1)
            zweite_zahl = randrange(2, viertel_von_minute + 1)
            ergebnis_erste_rechnung = erste_zahl * zweite_zahl
            dritte_zahl = minute / ergebnis_erste_rechnung

aufgabe_für_minute_ausgeben()
#print(ergebnis_erste_rechnung, zweiter_operator_für_minute, int(dritte_zahl))
#print(erste_zahl)
#print(zweite_zahl)
#print(dritte_zahl)
print(int(ergebnis_erste_rechnung))
print(minute)
