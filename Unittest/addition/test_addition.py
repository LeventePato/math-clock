import unittest
from helpers_addition import factor_addition_addition
from helpers_addition import factor_addition_subtraction
from helpers_addition import factor_addition_division
from helpers_addition import factor_addition_multiplication

class TestAdditionAddition(unittest.TestCase):
    def test_addition_addition(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_addition_addition(stunde)
            if x*y*z > 1:
                self.assertEqual(x+y+z, stunde)
            stunde = stunde + 1

class TestAdditionSubtraction(unittest.TestCase):
    def test_addition_subtraktion(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_addition_subtraction(stunde)
            self.assertEqual(x+y-z, stunde)
            stunde = stunde + 1

class TestAdditionDivision(unittest.TestCase):
    def test_addition_division(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_addition_division(stunde)
            if x*y*z > 1:
                self.assertEqual(y/z+x, stunde)
            stunde = stunde + 1

class TestAdditionMultiplication(unittest.TestCase):
    def test_addition_multplication(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_addition_multiplication(stunde)
            if x*y*z > 1:
                self.assertEqual(x+y*z, stunde)
            stunde = stunde + 1


if __name__ == '__main__':
    unittest.main()
