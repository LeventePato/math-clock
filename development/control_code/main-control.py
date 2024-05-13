from time import sleep
from datetime import datetime

show_time = True

while show_time == True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    sleep(10)

