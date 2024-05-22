import random
import functions

erster_operator_für_stunde = "  "
zweiter_operator_für_stunde = "  "

def aufgabe_für_stunde(stunde):
    
    while True:
        erste_operation_für_stunde = random.randrange(1, 5)
        zweite_operation_für_stunde = random.randrange(1, 5)
        if erste_operation_für_stunde == 1:
            erster_operator_für_stunde = " + "
            if zweite_operation_für_stunde == 1:
                zweiter_operator_für_stunde = " + "
                zahlen = functions.stunde_addition_addition(stunde)
            elif zweite_operation_für_stunde == 2:
                zweiter_operator_für_stunde = " - "
                zahlen = functions.stunde_addition_subtraction(stunde)
            elif zweite_operation_für_stunde == 3:
                zweiter_operator_für_stunde = " : "
                zahlen = functions.stunde_addition_division(stunde)
            else:
                zweiter_operator_für_stunde = " x "
                zahlen = functions.stunde_addition_multiplication(stunde)

        elif erste_operation_für_stunde == 2:
            erster_operator_für_stunde = " - "
            if zweite_operation_für_stunde == 1:
                zweiter_operator_für_stunde = " + "
                zahlen = functions.stunde_subtraction_addition(stunde)
            elif zweite_operation_für_stunde == 2:
                zweiter_operator_für_stunde = " - "
                zahlen = functions.stunde_subtraction_subtraction(stunde)
            elif zweite_operation_für_stunde == 3:
                zweiter_operator_für_stunde = " : "
                zahlen = functions.stunde_subtraction_division(stunde)
            else:
                zweiter_operator_für_stunde = " x "
                zahlen = functions.stunde_subtraction_multiplication(stunde)

        elif erste_operation_für_stunde == 3:
            erster_operator_für_stunde = " : "
            if zweite_operation_für_stunde == 1:
                zweiter_operator_für_stunde = " + "
                zahlen = functions.stunde_division_addition(stunde)
            elif zweite_operation_für_stunde == 2:
                zweiter_operator_für_stunde = " - "
                zahlen = functions.stunde_division_subtraction(stunde)
            elif zweite_operation_für_stunde == 3:
                zweiter_operator_für_stunde = " : "
                zahlen = functions.stunde_division_division(stunde)
            else:
                zweiter_operator_für_stunde = " x "
                zahlen = functions.stunde_division_multiplication(stunde)

        else:
            erster_operator_für_stunde = " x "
            if zweite_operation_für_stunde == 1:
                zweiter_operator_für_stunde = " + "
                zahlen = functions.stunde_multiplication_addition(stunde)
            elif zweite_operation_für_stunde == 2:
                zweiter_operator_für_stunde = " - "
                zahlen = functions.stunde_multiplication_subtraction(stunde)
            elif zweite_operation_für_stunde == 3:
                zweiter_operator_für_stunde = " : "
                zahlen = functions.stunde_multiplication_division(stunde)
            else:
                zweiter_operator_für_stunde = " x "
                zahlen = functions.stunde_multiplication_multiplication(stunde) 

        if zahlen[0] * zahlen[1] * zahlen[2] > 1:
                return zahlen[0], erster_operator_für_stunde, zahlen[1], zweiter_operator_für_stunde, zahlen[2]

def aufgabe_für_minute(minute):

    while True:
        erste_operation_für_minute = random.randrange(1, 5)
        zweite_operation_für_minute = random.randrange(1, 5)
        if erste_operation_für_minute == 1:
            erster_operator_für_minute = " + "
            if zweite_operation_für_minute == 1:
                zweiter_operator_für_minute = " + "
                zahlen = functions.minute_addition_addition(minute)
            elif zweite_operation_für_minute == 2:
                zweiter_operator_für_minute = " - "
                zahlen = functions.minute_addition_subtraction(minute)
            elif zweite_operation_für_minute == 3:
                zweiter_operator_für_minute = " : "
                zahlen = functions.minute_addition_division(minute)
            else:
                zweiter_operator_für_minute = " x "
                zahlen = functions.minute_addition_multiplication(minute)

        elif erste_operation_für_minute == 2:
            erster_operator_für_minute = " - "
            if zweite_operation_für_minute == 1:
                zweiter_operator_für_minute = " + "
                zahlen = functions.minute_subtraction_addition(minute)
            elif zweite_operation_für_minute == 2:
                zweiter_operator_für_minute = " - "
                zahlen = functions.minute_subtraction_subtraction(minute)
            elif zweite_operation_für_minute == 3:
                zweiter_operator_für_minute = " : "
                zahlen = functions.minute_subtraction_division(minute)
            else:
              zweiter_operator_für_minute = " x "
              zahlen = functions.minute_subtraction_multiplication(minute)

        elif erste_operation_für_minute == 3:
            erster_operator_für_minute = " : "
            if zweite_operation_für_minute == 1:
                zweiter_operator_für_minute = " + "
                zahlen = functions.minute_division_addition(minute)
            elif zweite_operation_für_minute == 2:
                zweiter_operator_für_minute = " - "
                zahlen = functions.minute_division_subtraction(minute)
            elif zweite_operation_für_minute == 3:
                zweiter_operator_für_minute = " : "
                zahlen = functions.minute_division_division(minute)
            else:
              zweiter_operator_für_minute = " x "
              zahlen = functions.minute_division_multiplication(minute)

        else:
            erster_operator_für_minute = " x "
            if zweite_operation_für_minute == 1:
                zweiter_operator_für_minute = " + "
                zahlen = functions.minute_multiplication_addition(minute)
            elif zweite_operation_für_minute == 2:
                zweiter_operator_für_minute = " - "
                zahlen = functions.minute_multiplication_subtraction(minute)
            elif zweite_operation_für_minute == 3:
                zweiter_operator_für_minute = " : "
                zahlen = functions. minute_multiplication_division(minute)
            else:
                zweiter_operator_für_minute = " x "
                zahlen = functions.minute_multiplication_multiplication(minute)#
        
        if zahlen[0] * zahlen[1] * zahlen[2] > 1:
            return zahlen[0], erster_operator_für_minute, zahlen[1], zweiter_operator_für_minute, zahlen[2]