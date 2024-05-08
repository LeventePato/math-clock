import unittest
from random import randrange
from helpers_division import factor_division_addition
from helpers_division import count_factors


variables = {}
base_name = 'factors_of_'
for i in range(1,24):
    key = f'{base_name}{i}'
    variables[key] = count_factors(i) 
# from helpers_division import factor_division_subtraction
# from development.helpers_division import factor_division_division
# from development.helpers_division import factor_division_multiplication


#stunde = randrange(1, 25)
#class TestDivisionAddition(unittest.TestCase):
#    def test_division_addition(self):
#        x,y,z = factor_division_addition(1)
#        self.assertEqual(factor_division_addition(x/y+z),1)

# class TestDivisionSubtraction(unittest.TestCase):
#     def test_division_subtraktion(self):
#         self.assertEqual(factor_division_subtraction, stunde)

# class TestDivisionDivision(unittest.TestCase):
#     def test_division_subtraction(self):
#         self.assertEqual(factor_division_multiplication, stunde)

# class TestDivisionMultiplication(unittest.Testcase):
#     def test_division_subtraction(self):
#         self.ass



#if __name__ == '__main_division__':
#
#    unittest.main()


print(variables)
print(variables['factor_of_1'])
print(variables['factor_of_2'])
print(variables['factor_of_3'])
print(variables['factor_of_4'])
print(variables['factor_of_5'])
print(variables['factor_of_6'])
print(variables['factor_of_7'])
print(variables['factor_of_8'])
print(variables['factor_of_9'])
print(variables['factor_of_10'])
print(variables['factor_of_11'])
print(variables['factor_of_12'])
print(variables['factor_of_13'])
print(variables['factor_of_14'])
print(variables['factor_of_15'])
print(variables['factor_of_16'])
print(variables['factor_of_17'])
print(variables['factor_of_18'])
print(variables['factor_of_19']) 
print(variables['factor_of_20'])
print(variables['factor_of_21'])
print(variables['factor_of_22'])
print(variables['factor_of_23'])
