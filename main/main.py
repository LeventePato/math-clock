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

alle_zweite_operatoren_für_stunde = [[i]for i in range(1, 6)]
alle_zweite_operatoren_für_stunde[1] = " + "
alle_zweite_operatoren_für_stunde[2] = " - "
alle_zweite_operatoren_für_stunde[3] = " : "
alle_zweite_operatoren_für_stunde[4] = " x "


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
    stunde_string = now.strftime("%H")
    stunde = int(stunde_string)

    erste_operation_für_stunde = random.randrange(1, 5)
    zweite_operation_für_stunde = random.randrange(1, 5)

#    if erste_operation_für_stunde == 1:
#        if zweite_operation_für_stunde == 1:
#            zahlen_stunde = helpers.stunde_addition_addition(stunde)
#
#        elif zweite_operation_für_stunde == 2:
#            zahlen_stunde = helpers.stunde_addition_subtraction(stunde)
#
#        elif zweite_operation_für_stunde == 3: 
#            zahlen_stunde = helpers.stunde_addition_division(stunde)
#
#        else: 
#            zahlezahlen_stunden = helpers.stunde_addition_multiplication(stunde)
#
#    elif erste_operation_für_stunde == 2:
#        if zweite_operation_für_stunde == 1:
#            zahlen_stunde = helpers.stunde_subtraction_addition(stunde)
#
#        elif zweite_operation_für_stunde == 2:
#            zahzahlen_stundelen = helpers.stunde_subtraction_subtraction(stunde)
#
#        elif zweite_operation_für_stunde == 3:
#            zahlen_stunde = helpers.stunde_subtraction_division(stunde)
#
#        else: 
#            zahlen_stunde = helpers.stunde_subtraction_multiplication(stunde)
#
#    elif erste_operation_für_stunde == 3:
#        if zweite_operation_für_stunde == 1:
#            zahzahlen_stundeen = helpers.stunde_division_addition(stunde)
#    
#        elif zweite_operation_für_stunde == 2:
#            zahlen_stunde = helpers.stunde_division_subtraction(stunde)
#
#        elif zweite_operation_für_stunde == 3:
#            zahlen_stunde = helpers.stunde_division_division(stunde)
#
#        else: 
#            zahlen_stunde = helpers.stunde_division_multiplication(stunde)
#
#    else:
#        if zweite_operation_für_stunde:
#            zahlen_stunde = helpers.stunde_multiplication_addition(stunde)
#
#        elif zweite_operation_für_stunde:
#            zahlen_stunde = helpers.stunde_multiplication_subtraction(stunde)
#
#        elif zweite_operation_für_stunde:
#            zahlen_stunde = helpers.stunde_multiplication_division(stunde)
#
#        else:
#            zahlen_stunde = helpers.stunde_multiplication_multiplication(stunde)

    now = datetime.now()
    minute_string = now.strftime("%M")
    minute = int(minute_string)

    erste_operation_für_minute = random.randrange(1, 5)
    zweite_operation_für_minute = random.randrange(1, 5)

#    if erste_operation_für_minute == 1:
#        if zweite_operation_für_minute == 1:
#            zahlen_minute = helpers.minute_addition_addition(minute)
#
#        elif zweite_operation_für_minute == 2:
#            zahlen_minute = helpers.minute_addition_subtraction(minute)
#
#        elif zweite_operation_für_minute == 3: 
#            zahlen_minute = helpers.minute_addition_division(minute)
#
#        else: 
#            zahlen_minute = helpers.minute_addition_multiplication(minute)
#
#    elif erste_operation_für_minute == 2:
#        if zweite_operation_für_minute == 1:
#            zahlen_minute = helpers.minute_subtraction_addition(minute)
#
#        elif zweite_operation_für_minute == 2:
#            zahlen_minute = helpers.minute_subtraction_subtraction(minute)
#
#        elif zweite_operation_für_minute == 3:
#            zahlen_minute = helpers.minute_subtraction_division(minute)
#
#        else: 
#            zahlezahlen_minuten = helpers.minute_subtraction_multiplication(minute)
#
#    elif erste_operation_für_minute == 3:
#        if zweite_operation_für_minute == 1:
#            zahlen_minute = helpers.minute_division_addition(minute)
#    
#        elif zweite_operation_für_minute == 2:
#            zahlen_minute = helpers.minute_division_subtraction(minute)
#
#        elif zweite_operation_für_minute == 3:
#            zahlen_minute = helpers.minute_division_division(minute)
#
#        else: 
#            zahlen_minute = helpers.minute_division_multiplication(minute)
#
#    else:
#        if zweite_operation_für_minute:
#            zahlen_minute = helpers.minute_multiplication_addition(minute)
#
#        elif zweite_operation_für_minute:
#            zahlen_minute = helpers.minute_multiplication_subtraction(minute)
#
#        elif zweite_operation_für_minute:
#            zahlen_minute = helpers.minute_multiplication_division(minute)
#
#        else:
#            zahlen_minute = helpers.minute_multiplication_multiplication(minute)

#    gesamt_stunde = 1
#    for zahl_stunde in zahlen_stunde:
#        gesamt_stunde *= zahl_stunde
#    if gesamt_stunde == 1:
#        print("False")
#    
#    gesamt_minute = 1
#    for zahl_minute in zahlen_minute:
#        gesamt_minute *= zahl_minute
#    if gesamt_minute == 1:
#        print("False")

    zahlen_stunde = int(main2.aufgabe_für_stunde(stunde, erste_operation_für_stunde, zweite_operation_für_stunde))
    zahlen_minute = int(main2.aufgabe_für_minute(minute, erste_operation_für_minute, zweite_operation_für_minute))

    erste_zahl_stunde = zahlen_stunde[0]
    zweite_zahl_minute = zahlen_stunde[1]
    dritte_zahl_minute = zahlen_stunde[2]


    
    sleep(1)

    erster_operator_für_stunde = alle_erste_operationen_für_stunde[erste_operation_für_stunde]
    zweiter_operator_für_stunde = alle_zweite_operatoren_für_stunde[zweite_operation_für_stunde]
    
    helpers.aufgabe_für_stunde_ausgeben(erster_operator_für_stunde, zweiter_operator_für_stunde, )
    
    
    erster_operator_für_minute = alle_erste_operationen_für_minute[erste_operation_für_minute]
    zweiter_operator_für_minute = alle_zweite_operatoren_für_minute[zweite_operation_für_minute]

    helpers.aufgabe_für_minute_ausgeben(erster_operator_für_minute, zweiter_operator_für_minute, zahlen_minute[0], zahlen_minute[1], zahlen_minute[2])