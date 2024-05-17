import unittest
from random import randrange
from helpers_multiplication import factor_multiplication_addition
from helpers_multiplication import factor_multiplication_subtraction
from helpers_multiplication import factor_multiplication_division
from helpers_multiplication import factor_multiplication_multiplication

faktoren = [[] for _ in range(100)]

for i in range(2, 100):
    for j in range(2, int(i/2 + 1)):
        if i % j == 0:
            faktoren[i].append(j)

prime_numbers = []

for i in range(2, 100):
    prime = (len(faktoren[i]) == 0)
    if prime == True:
        prime_numbers.append(i)


def teilbarkeit(n):
    for i in range(4, int(n / 2) + 1):
        if i not in faktoren[n]:
            teilbar = False
        else:
            teilbar = True
            return teilbar


class TestMultiplicationAddition(unittest.TestCase):
    def test_multiplication_addition(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_multiplication_addition(stunde)
            if x*y*z > 1:
                self.assertEqual(x*y+z, stunde)
            stunde = stunde + 1

class TestMultiplicationSubtraction(unittest.TestCase):
    def test_multplication_subtraktion(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_multiplication_subtraction(stunde)
            self.assertEqual(x*y-z, stunde)
            stunde = stunde + 1

class TestMultiplicationDivision(unittest.TestCase):
    def test_multplication_division(self):
        stunde = 0        
        while stunde < 24:
            x,y,z = factor_multiplication_division(stunde)
            if x*y*z > 1:
                self.assertEqual(x*y/z, stunde)
            stunde = stunde + 1
class TestMultiplicationMultiplication(unittest.TestCase):
    def test_multplication_multplication(self):
        stunde = 0
        while stunde < 24:
            x,y,z = factor_multiplication_multiplication(stunde)
            if x*y*z > 1:
                self.assertEqual(x*y*z, stunde)
            stunde = stunde + 1


if __name__ == '__main__':
    unittest.main()