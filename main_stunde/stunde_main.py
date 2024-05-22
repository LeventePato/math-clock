import random
from time import sleep
from datetime import datetime
import stunde_helpers


alle_erste_operationen_für_stunde = [str for i in range(1, 6)]
alle_erste_operationen_für_stunde[1] = " + "
alle_erste_operationen_für_stunde[2] = " - "
alle_erste_operationen_für_stunde[3] = " : "
alle_erste_operationen_für_stunde[4] = " x "

alle_zweite_operatoren_für_stunde = [[i]for i in range(1, 6)]
alle_zweite_operatoren_für_stunde[1] = " + "
alle_zweite_operatoren_für_stunde[2] = " - "
alle_zweite_operatoren_für_stunde[3] = " : "
alle_zweite_operatoren_für_stunde[4] = " x "


while 1 == 1:
    
    now = datetime.now()
    stunde_string = now.strftime("%H")
    stunde = int(stunde_string)

    erste_operation_für_stunde = random.randrange(1, 5)
    zweite_operation_für_stunde = random.randrange(1, 5)

    if erste_operation_für_stunde == 1:
        if zweite_operation_für_stunde == 1:
            zahlen = stunde_helpers.factor_addition_addition(stunde)

        elif zweite_operation_für_stunde == 2:
            zahlen = stunde_helpers.factor_addition_subtraction(stunde)

        elif zweite_operation_für_stunde == 3: 
            zahlen = stunde_helpers.factor_addition_division(stunde)

        else: 
            zahlen = stunde_helpers.factor_addition_multiplication(stunde)

    elif erste_operation_für_stunde == 2:
        if zweite_operation_für_stunde == 1:
            zahlen = stunde_helpers.factor_subtraction_addition(stunde)

        elif zweite_operation_für_stunde == 2:
            zahlen = stunde_helpers.factor_subtraction_subtraction(stunde)

        elif zweite_operation_für_stunde == 3:
            zahlen = stunde_helpers.factor_subtraction_division(stunde)

        else: 
            zahlen = stunde_helpers.factor_subtraction_multiplication(stunde)

    elif erste_operation_für_stunde == 3:
        if zweite_operation_für_stunde == 1:
            zahlen = stunde_helpers.factor_division_addition(stunde)
    
        elif zweite_operation_für_stunde == 2:
            zahlen = stunde_helpers.factor_division_subtraction(stunde)

        elif zweite_operation_für_stunde == 3:
            zahlen = stunde_helpers.factor_division_division(stunde)

        else: 
            zahlen = stunde_helpers.factor_division_multiplication(stunde)

    else:
        if zweite_operation_für_stunde:
            zahlen = stunde_helpers.factor_multiplication_addition(stunde)

        elif zweite_operation_für_stunde:
            zahlen = stunde_helpers.factor_multiplication_subtraction(stunde)

        elif zweite_operation_für_stunde:
            zahlen = stunde_helpers.factor_multiplication_division(stunde)

        else:
            zahlen = stunde_helpers.factor_multiplication_multiplication(stunde)

    sleep(5)

    erster_operator_für_stunde = alle_erste_operationen_für_stunde[erste_operation_für_stunde]
    zweiter_operator_für_stunde = alle_zweite_operatoren_für_stunde[zweite_operation_für_stunde]
    erste_zahl = str(zahlen[0])
    zweite_zahl = str(zahlen[1])
    dritte_zahl = str(zahlen[2])

    stunde_helpers.aufgabe_für_stunde(erster_operator_für_stunde, zweiter_operator_für_stunde, erste_zahl, zweite_zahl, dritte_zahl)