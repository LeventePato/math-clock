import unittest
from random import randrange
from helpers_division import factor_division_addition
from helpers_division import factor_division_subtraction
from helpers_division import factor_division_division
from helpers_division import factor_division_multiplication
from helpers_division import count_factors

class TestDivisionAddition(unittest.TestCase):
    def test_division_addition(self):
        stunde = 4
        while stunde < 24:
            stunde = stunde + 1
            x,y,z = factor_division_addition(stunde)
            self.assertEqual(x/y+z, stunde)

class TestDivisionSubtraction(unittest.TestCase):
    def test_division_subtraktion(self):
        stunde = 1
        while stunde < 24:
            stunde = stunde + 1
            x,y,z = factor_division_subtraction(stunde)
            self.assertEqual(x/y-z, stunde)

class TestDivisionDivision(unittest.TestCase):
    def test_division_division(self):
        stunde = 1        
        while stunde < 24:
            stunde = stunde + 1
            x,y,z = factor_division_division(stunde)
            self.assertEqual(x/y/z, stunde)

class TestDivisionMultiplication(unittest.TestCase):
    def test_division_multplication(self):
        stunde = 1
        while stunde < 24:
            while count_factors(stunde) < 3:    
                stunde = stunde + 1
            x,y,z = factor_division_multiplication(stunde)
            self.assertEqual(x/y*z, stunde)
            stunde = stunde + 1

        
if __name__ == '__main__':
    unittest.main()