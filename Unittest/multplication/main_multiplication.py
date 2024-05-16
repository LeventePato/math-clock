from random import randrange
from helpers_multiplication import factor_multiplication_addition
from helpers_multiplication import factor_multiplication_subtraction
#from helpers_multiplication import factor_multiplication_division
#from helpers_multiplication import factor_multiplication_multiplication

stunde = randrange(1, 24)
erste_operation_für_stunde = 4
zweite_operation_für_stunde = randrange(1, 5)

if erste_operation_für_stunde == 4:
    if zweite_operation_für_stunde == 1:
        factor_multiplication_addition(stunde)
    
    elif zweite_operation_für_stunde == 2:
        factor_multiplication_subtraction(stunde)

#    elif zweite_operation_für_stunde == 3:
 #       factor_multiplication_division(stunde)

#    else:
 #       factor_multiplication_multiplication(stunde)