if erste_operatoration_für_stunde == 4:
    def multiplikationsaufgabe_lösen():
        print(erste_zahl, "*", zweite_zahl)

    hälfte_von_stunde = stunde / 2 + 1
    erste_zahl = 100
    while stunde % erste_zahl > 0:
        erste_zahl = randrange(2, hälfte_von_stunde)
        multiplikations_aufgabe = erste_zahl * zweite_zahl
    multiplikationsaufgabe_lösen()


