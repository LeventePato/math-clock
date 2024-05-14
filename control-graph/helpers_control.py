from time import sleep
from datetime import datetime

def track_time():
    show_time = True
    while show_time == True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        sleep(10)

aufgabe_für_stunde =  10 * 4 / 20