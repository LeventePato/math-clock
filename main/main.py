import helpers
import main2
import random
from datetime import datetime
from time import sleep

alle_erste_operationen_für_stunde = [str for i in range(1, 6)]
alle_erste_operationen_für_stunde[1] = " + "
alle_erste_operationen_für_stunde[2] = " - "
alle_erste_operationen_für_stunde[3] = " : "
alle_erste_operationen_für_stunde[4] = " x "

alle_zweite_operatoren_für_stunde = [str for i in range(1, 6)]
alle_zweite_operatoren_für_stunde[1] = " + "
alle_zweite_operatoren_für_stunde[2] = " - "
alle_zweite_operatoren_für_stunde[3] = " : "
alle_zweite_operatoren_für_stunde[4] = " x "


alle_erste_operationen_für_minute = [str for i in range(1, 6)]
alle_erste_operationen_für_minute[1] = " + "
alle_erste_operationen_für_minute[2] = " - "
alle_erste_operationen_für_minute[3] = " : "
alle_erste_operationen_für_minute[4] = " x "

alle_zweite_operatoren_für_minute = [str for i in range(1, 6)]
alle_zweite_operatoren_für_minute[1] = " + "
alle_zweite_operatoren_für_minute[2] = " - "
alle_zweite_operatoren_für_minute[3] = " : "
alle_zweite_operatoren_für_minute[4] = " x "



while 1 == 1:
    
    now = datetime.now()
    stunde_string = now.strftime("%H")
    stunde = int(stunde_string)

    erste_operation_für_stunde = random.randrange(1, 5)
    zweite_operation_für_stunde = random.randrange(1, 5)


    now = datetime.now()
    minute_string = now.strftime("%M")
    minute = int(minute_string)

    erste_operation_für_minute = random.randrange(1, 5)
    zweite_operation_für_minute = random.randrange(1, 5)


    operation_stunde = main2.aufgabe_für_stunde(stunde)
    zahlen_minute = main2.aufgabe_für_minute(minute)

    erste_zahl_stunde = str(operation_stunde[0])
    zweite_zahl_stunde = str(operation_stunde[1])
    dritte_zahl_stunde = str(operation_stunde[2])
    erste_operation_für_stunde = operation_stunde[3]
    zweite_operation_für_stunde = operation_stunde[4]

    erste_zahl_minute = str(zahlen_minute[0])
    zweite_zahl_minute = str(zahlen_minute[1])
    dritte_zahl_minute = str(zahlen_minute[2])
    
    sleep(0.1)

    erster_operator_für_stunde = alle_erste_operationen_für_stunde[erste_operation_für_stunde - 1]
    zweiter_operator_für_stunde = alle_zweite_operatoren_für_stunde[zweite_operation_für_stunde - 1]
    
    print(stunde)
    helpers.aufgabe_für_stunde_ausgeben(erster_operator_für_stunde, zweiter_operator_für_stunde, operation_stunde)
    
    
    erster_operator_für_minute = alle_erste_operationen_für_minute[erste_operation_für_minute]
    zweiter_operator_für_minute = alle_zweite_operatoren_für_minute[zweite_operation_für_minute]
    
    print(minute)
    helpers.aufgabe_für_minute_ausgeben(erster_operator_für_minute, zweiter_operator_für_minute, operation_stunde)
    print ("-----------")