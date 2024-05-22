import unittest
from helpers_subtraction import factor_subtraction_addition
from helpers_subtraction import factor_subtraction_subtraction
from helpers_subtraction import factor_subtraction_division
from helpers_subtraction import factor_subtraction_multiplication

class TestSubtractionAddition(unittest.TestCase):
    def test_subtraction_addition(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_subtraction_addition(stunde)
            if x*y*z > 1:
                self.assertEqual(x-y+z, stunde)
            stunde = stunde + 1

class TestSubtractionSubtraction(unittest.TestCase):
    def test_subtraction_subtraktion(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_subtraction_subtraction(stunde)
            self.assertEqual(x-y-z, stunde)
            stunde = stunde + 1

class TestSubtractionDivision(unittest.TestCase):
    def test_subtraction_division(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_subtraction_division(stunde)
            self.assertEqual(x-(y/z), stunde)
            stunde = stunde + 1

class TestSubtractionMultiplication(unittest.TestCase):
    def test_subtraction_multplication(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_subtraction_multiplication(stunde)
            if x*y*z > 1:
                self.assertEqual(x-(y*z), stunde)
            stunde = stunde + 1

        
if __name__ == '__main__':
    unittest.main()