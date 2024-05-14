from helpers_addition import factors_addition_addition
from helpers_addition import factors_addition_subtraction
from helpers_addition import factors_addition_division
from helpers_addition import factors_addition_multiplication
from helpers_addition import count_factors

stunde = 1

erste_operation_für_stunde = 1
zweite_operation_für_stunde = 1

if erste_operation_für_stunde == 1:
    erster_operator_für_stunde = "+"

    if zweite_operation_für_stunde == 1:
        zweiter_operator_für_stunde = "+"

        factors_addition_addition(stunde)

    elif zweite_operation_für_stunde == 2:
        zweiter_operator_für_stunde = "-"

        factors_addition_subtraction(stunde)

    elif zweite_operation_für_stunde == 3:
        zweiter_operator_für_stunde = ":"

        factors_addition_division(stunde)

    else:
        zweiter_operator_für_stunde = "x"

        factors_addition_multiplication(stunde)