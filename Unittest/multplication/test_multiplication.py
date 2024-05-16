import unittest
from random import randrange
from helpers_multiplication import factor_multiplication_addition
from helpers_multiplication import factor_multiplication_subtraction
#from helpers_multiplication import factor_multiplication_division
#from helpers_multiplication import factor_multiplication_multiplication
from helpers_multiplication import count_factors

class TestMultiplicationAddition(unittest.TestCase):
    def test_multiplication_addition(self):
        stunde = 6
        while stunde < 24:
            x,y,z = factor_multiplication_addition(stunde)
            self.assertEqual(x*y+z, stunde)
            stunde = stunde + 1

class TestMultiplicationSubtraction(unittest.TestCase):
    def test_multplication_subtraktion(self):
        stunde = 1
        while stunde < 24:
            x,y,z = factor_multiplication_subtraction(stunde)
            self.assertEqual(x*y-z, stunde)
            stunde = stunde + 1

#class TestMultiplicationDivision(unittest.TestCase):
 #   def test_multplication_division(self):
  #      stunde = 1        
   #     while stunde < 24:
    #        stunde = stunde + 1
     #       x,y,z = factor_multiplication_division(stunde)
      #      self.assertEqual(x*y/z, stunde)

#class TestMultiplicationMultiplication(unittest.TestCase):
 #   def test_multplication_multplication(self):
  #      stunde = 1
   #     while stunde < 24:
    #        while count_factors(stunde) < 3:    
     #           stunde = stunde + 1
      #      x,y,z = factor_multiplication_multiplication(stunde)
       #     self.assertEqual(x*y*z, stunde)
        #    stunde = stunde + 1

        
if __name__ == '__main__':
    unittest.main()