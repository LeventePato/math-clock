import unittest
from random import randrange
from helpers_subtraction import factor_subtraction_addition
from helpers_subtraction import factor_subtraction_subtraction
from helpers_subtraction import factor_subtraction_division
from helpers_subtraction import factor_subtraction_multiplication
from helpers_subtraction import count_factors

class TestSubtractionAddition(unittest.TestCase):
    def test_subtraction_addition(self):
        stunde = 3
        while stunde < 24:
            stunde = stunde + 1
            x,y,z = factor_subtraction_addition(stunde)
            self.assertEqual(x-y+z, stunde)

class TestSubtractionSubtraction(unittest.TestCase):
    def test_subtraction_subtraktion(self):
        stunde = 1
        while stunde < 24:
            stunde = stunde + 1
            x,y,z = factor_subtraction_subtraction(stunde)
            self.assertEqual(x-y-z, stunde)

class TestSubtractionDivision(unittest.TestCase):
    def test_subtraction_division(self):
        stunde = 1
        while stunde < 24:
            stunde = stunde + 1
            x,y,z = factor_subtraction_division(stunde)
            self.assertEqual(x-y/z, stunde)

class TestSubtractionMultiplication(unittest.TestCase):
    def test_subtraction_multplication(self):
        stunde = 1
        while stunde < 24:
            while count_factors(stunde) < 3:    
                stunde = stunde + 1
            x,y,z = factor_subtraction_multiplication(stunde)
            self.assertEqual(x-y*z, stunde)
            stunde = stunde + 1

        
if __name__ == '__main__':
    unittest.main()