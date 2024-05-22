import helpers

while True:
    for stunde in range(0, 24):
        for minute in range(0, 60):
            hour_encoded = helpers.aufgabe_für_stunde(stunde)
            minute_encoded = helpers.aufgabe_für_minute(minute)
            print ("%d:%d" % (stunde, minute))
            print ("%d%s%d%s%d h\n%d%s%d%s%d m" % (hour_encoded[0], hour_encoded[1], hour_encoded[2], hour_encoded[3], hour_encoded[4], minute_encoded[0], minute_encoded[1], minute_encoded[2], minute_encoded[3], minute_encoded[4]))
            print("_______________")
