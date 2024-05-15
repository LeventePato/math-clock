from random import randrange
from helpers_addition import factor_addition_addition
from helpers_addition import factor_addition_subtraction
from helpers_addition import factor_addition_division
from helpers_addition import factor_addition_multiplication

stunde = 1

erste_operation_für_stunde = 1
zweite_operation_für_stunde = randrange(1, 5)

if erste_operation_für_stunde == 1:
    
    if zweite_operation_für_stunde == 1:
        factor_addition_addition(stunde)

    elif zweite_operation_für_stunde == 2:
        factor_addition_subtraction(stunde)

    elif zweite_operation_für_stunde == 3:
        factor_addition_division(stunde)

    else:
        factor_addition_multiplication(stunde)