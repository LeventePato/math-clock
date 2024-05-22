import random
from time import sleep
from datetime import datetime
import minute_helpers


alle_erste_operationen_für_minute = [str for i in range(1, 6)]
alle_erste_operationen_für_minute[1] = " + "
alle_erste_operationen_für_minute[2] = " - "
alle_erste_operationen_für_minute[3] = " : "
alle_erste_operationen_für_minute[4] = " x "

alle_zweite_operatoren_für_minute = [[i]for i in range(1, 6)]
alle_zweite_operatoren_für_minute[1] = " + "
alle_zweite_operatoren_für_minute[2] = " - "
alle_zweite_operatoren_für_minute[3] = " : "
alle_zweite_operatoren_für_minute[4] = " x "


while 1 == 1:
    
    now = datetime.now()
    minute_string = now.strftime("%M")
    minute = int(minute_string)

    erste_operation_für_minute = random.randrange(1, 5)
    zweite_operation_für_minute = random.randrange(1, 5)

    if erste_operation_für_minute == 1:
        if zweite_operation_für_minute == 1:
            zahlen = minute_helpers.factor_addition_addition(minute)

        elif zweite_operation_für_minute == 2:
            zahlen = minute_helpers.factor_addition_subtraction(minute)

        elif zweite_operation_für_minute == 3: 
            zahlen = minute_helpers.factor_addition_division(minute)

        else: 
            zahlen = minute_helpers.factor_addition_multiplication(minute)

    elif erste_operation_für_minute == 2:
        if zweite_operation_für_minute == 1:
            zahlen = minute_helpers.factor_subtraction_addition(minute)

        elif zweite_operation_für_minute == 2:
            zahlen = minute_helpers.factor_subtraction_subtraction(minute)

        elif zweite_operation_für_minute == 3:
            zahlen = minute_helpers.factor_subtraction_division(minute)

        else: 
            zahlen = minute_helpers.factor_subtraction_multiplication(minute)

    elif erste_operation_für_minute == 3:
        if zweite_operation_für_minute == 1:
            zahlen = minute_helpers.factor_division_addition(minute)
    
        elif zweite_operation_für_minute == 2:
            zahlen = minute_helpers.factor_division_subtraction(minute)

        elif zweite_operation_für_minute == 3:
            zahlen = minute_helpers.factor_division_division(minute)

        else: 
            zahlen = minute_helpers.factor_division_multiplication(minute)

    else:
        if zweite_operation_für_minute:
            zahlen = minute_helpers.factor_multiplication_addition(minute)

        elif zweite_operation_für_minute:
            zahlen = minute_helpers.factor_multiplication_subtraction(minute)

        elif zweite_operation_für_minute:
            zahlen = minute_helpers.factor_multiplication_division(minute)

        else:
            zahlen = minute_helpers.factor_multiplication_multiplication(minute)

    sleep(5)

    erster_operator_für_stunde = alle_erste_operationen_für_minute[erste_operation_für_minute]
    zweiter_operator_für_stunde = alle_zweite_operatoren_für_minute[zweite_operation_für_minute]
    erste_zahl = str(zahlen[0])
    zweite_zahl = str(zahlen[1])
    dritte_zahl = str(zahlen[2])

    minute_helpers.aufgabe_für_minute(erster_operator_für_stunde, zweiter_operator_für_stunde, erste_zahl, zweite_zahl, dritte_zahl)
