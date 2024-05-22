import unittest
from random import randrange
from development.testing_ground.helpers_division import factor_division_addition
# from development.helpers_division import factor_division_subtraction
# from development.helpers_division import factor_division_division
# from development.helpers_division import factor_division_multiplication

stunde = randrange(1, 25)

class TestDivisionAddition(unittest.TestCase):
    def test_division_addition(self):
        x,y,z = factor_division_addition(1)
        self.assertEqual(factor_division_addition(x/y+z),1)

# class TestDivisionSubtraction(unittest.TestCase):
#     def test_division_subtraktion(self):
#         self.assertEqual(factor_division_subtraction, stunde)

# class TestDivisionDivision(unittest.TestCase):
#     def test_division_subtraction(self):
#         self.assertEqual(factor_division_multiplication, stunde)

# class TestDivisionMultiplication(unittest.Testcase):
#     def test_division_subtraction(self):
#         self.ass
