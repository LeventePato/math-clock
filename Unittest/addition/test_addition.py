import unittest
from random import randrange
from helpers_addition import factor_addition_addition
from helpers_addition import factor_addition_subtraction
from helpers_addition import factor_addition_division
from helpers_addition import factor_addition_multiplication
from helpers_addition import count_factors

class TestAdditionAddition(unittest.TestCase):
    def test_addition_addition(self):
        stunde = 6
        while stunde < 24:
            stunde = stunde + 1
            x,y,z = factor_addition_addition(stunde)
            self.assertEqual(x+y+z, stunde)

#class TestAdditionSubtraction(unittest.TestCase):
 #   def test_addition_subtraktion(self):
  #      stunde = 2
   #     while stunde < 24:
    #        stunde = stunde + 1
     #       x,y,z = factor_addition_subtraction(stunde)
      #      self.assertEqual(x+y-z, stunde)

#class TestAdditionDivision(unittest.TestCase):
 #   def test_addition_division(self):
  #      stunde = 3
   #     while stunde < 24:
    #        stunde = stunde + 1
     #       x,y,z = factor_addition_division(stunde)
      #      self.assertEqual(x+y/z, stunde)

#class TestAdditionMultiplication(unittest.TestCase):
 #   def test_addition_multplication(self):
  #      stunde = 8
   #     while stunde < 24:
    #        while count_factors(stunde) < 3:    
     #           stunde = stunde + 1
      #      x,y,z = factor_addition_multiplication(stunde)
       #     self.assertEqual(x+y*z, stunde)
        #    stunde = stunde + 1

        
if __name__ == '__main__':
    unittest.main()