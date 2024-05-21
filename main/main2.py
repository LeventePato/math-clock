import helpers


def aufgabe_für_stunde(stunde, erste_operation_für_stunde, zweite_operation_für_stunde):
    if erste_operation_für_stunde == 1:
        if zweite_operation_für_stunde == 1:
            zahlen = helpers.stunde_addition_addition(stunde)
        elif zweite_operation_für_stunde == 2:
            zahlen = helpers.stunde_addition_subtraction(stunde)
        elif zweite_operation_für_stunde == 3: 
            zahlen = helpers.stunde_addition_division(stunde)
        else: 
            zahlen = helpers.stunde_addition_multiplication(stunde)
    elif erste_operation_für_stunde == 2:
        if zweite_operation_für_stunde == 1:
            zahlen = helpers.stunde_subtraction_addition(stunde)
        elif zweite_operation_für_stunde == 2:
            zahlen = helpers.stunde_subtraction_subtraction(stunde)
        elif zweite_operation_für_stunde == 3:
            zahlen = helpers.stunde_subtraction_division(stunde)
        else: 
            zahlen = helpers.stunde_subtraction_multiplication(stunde)
    elif erste_operation_für_stunde == 3:
        if zweite_operation_für_stunde == 1:
            zahlen = helpers.stunde_division_addition(stunde)
    
        elif zweite_operation_für_stunde == 2:
            zahlen = helpers.stunde_division_subtraction(stunde)
        elif zweite_operation_für_stunde == 3:
            zahlen = helpers.stunde_division_division(stunde)
        else: 
            zahlen = helpers.stunde_division_multiplication(stunde)
    else:
        if zweite_operation_für_stunde:
            zahlen = helpers.stunde_multiplication_addition(stunde)
        elif zweite_operation_für_stunde:
            zahlen = helpers.stunde_multiplication_subtraction(stunde)
        elif zweite_operation_für_stunde:
            zahlen = helpers.stunde_multiplication_division(stunde)
        else:
            zahlen = helpers.stunde_multiplication_multiplication(stunde)
    return zahlen



def aufgabe_für_minute(minute, erste_operation_für_minute, zweite_operation_für_minute):
    if erste_operation_für_minute == 1:
        if zweite_operation_für_minute == 1:
            zahlen = helpers.minute_addition_addition(minute)
        elif zweite_operation_für_minute == 2:
            zahlen = helpers.minute_addition_subtraction(minute)
        elif zweite_operation_für_minute == 3: 
            zahlen = helpers.minute_addition_division(minute)
        else: 
            zahlen = helpers.minute_addition_multiplication(minute)
    elif erste_operation_für_minute == 2:
        if zweite_operation_für_minute == 1:
            zahlen = helpers.minute_subtraction_addition(minute)
        elif zweite_operation_für_minute == 2:
            zahlen = helpers.minute_subtraction_subtraction(minute)
        elif zweite_operation_für_minute == 3:
            zahlen = helpers.minute_subtraction_division(minute)
        else: 
            zahlen = helpers.minute_subtraction_multiplication(minute)
    elif erste_operation_für_minute == 3:
        if zweite_operation_für_minute == 1:
            zahlen = helpers.minute_division_addition(minute)
        elif zweite_operation_für_minute == 2:
            zahlen = helpers.minute_division_subtraction(minute)
        elif zweite_operation_für_minute == 3:
            zahlen = helpers.minute_division_division(minute)
        else: 
            zahlen = helpers.minute_division_multiplication(minute)
    else:
        if zweite_operation_für_minute:
            zahlen = helpers.minute_multiplication_addition(minute)
        elif zweite_operation_für_minute:
            zahlen = helpers.minute_multiplication_subtraction(minute)
        elif zweite_operation_für_minute:
            zahlen = helpers.minute_multiplication_division(minute)
        else:
            zahlen = helpers.minute_multiplication_multiplication(minute)
    return zahlen
    

