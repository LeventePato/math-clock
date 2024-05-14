from random import randrange
from helpers_division import factor_division_addition
from helpers_division import factor_division_subtraction
from helpers_division import factor_division_division
from helpers_division import factor_division_multiplication

stunde = 16#randrange(1, 25)
hälfte_von_stunde = int(stunde / 2 + 1)

erste_operation_für_stunde = 3
zweite_operation_für_stunde = 4#randrange(1, 5)

if stunde % 2 > 0 and stunde % 3 > 0:
    zweite_operation_für_stunde = randrange(1, 4)

if stunde < 5:
    zweite_operation_für_stunde = randrange(2, 4)

if erste_operation_für_stunde == 3:
    erster_operator_für_stunde = ":"

    if zweite_operation_für_stunde == 1:
        factor_division_addition(stunde)

    elif zweite_operation_für_stunde == 2:
        factor_division_subtraction(stunde)

    elif zweite_operation_für_stunde == 3:
        factor_division_division(stunde)

    else:
        factor_division_multiplication(stunde)
