from datetime import datetime
import functions
import helpers
from time import sleep

while True:
    now = datetime.now()
    stunde_str = now.strftime("%H")
    stunde = int(stunde_str)

    minute_str = now.strftime("%M")
    minute = int(minute_str)

    print("    ", stunde, " : ", minute)

    print(helpers.aufgabe_für_stunde(stunde))
    print(helpers.aufgabe_für_minute(minute))

    sleep(0.5)

