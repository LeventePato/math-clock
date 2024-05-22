import unittest
from random import randrange
from helpers_division import factor_division_addition
from helpers_division import factor_division_subtraction
from helpers_division import factor_division_division
from helpers_division import factor_division_multiplication

class TestDivisionAddition(unittest.TestCase):
    def test_division_addition(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_division_addition(stunde)
            if x*y*z > 1:
                self.assertEqual(x/y+z, stunde)
            stunde = stunde + 1

class TestDivisionSubtraction(unittest.TestCase):
    def test_division_subtraktion(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_division_subtraction(stunde)
            if x*y*z > 1:
                self.assertEqual(x/y-z, stunde)
            stunde = stunde + 1

class TestDivisionDivision(unittest.TestCase):
    def test_division_division(self):
        stunde = 0        
        while stunde < 24:
            x,y,z = factor_division_division(stunde)
            if x*y*z > 1:
                self.assertEqual(x/y/z, stunde)
            stunde = stunde + 1

class TestDivisionMultiplication(unittest.TestCase):
    def test_division_multplication(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_division_multiplication(stunde)
            if x*y*z > 1:    
                self.assertEqual(x/y*z, stunde)
            stunde = stunde + 1

        
if __name__ == '__main__':
    unittest.main()