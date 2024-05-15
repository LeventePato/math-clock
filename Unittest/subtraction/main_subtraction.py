from random import randrange
from helpers_subtraction import factor_subtraction_addition
from helpers_subtraction import factor_subtraction_subtraction
from helpers_subtraction import factor_subtraction_division
from helpers_subtraction import factor_subtraction_multiplication

stunde = randrange(1, 24)
erste_operation_für_stunde = 2
zweite_operation_für_stunde = randrange(1, 5)

if erste_operation_für_stunde == 2:

    if zweite_operation_für_stunde == 1: 
        factor_subtraction_addition(stunde)

    elif zweite_operation_für_stunde == 2: 
        factor_subtraction_subtraction(stunde)

    elif zweite_operation_für_stunde == 3: 
        factor_subtraction_division(stunde)

    else:
        factor_subtraction_multiplication(stunde)
