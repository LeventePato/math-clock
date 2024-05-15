import unittest
from random import randrange
from division.helpers_division import factor_division_addition
from division.helpers_division import count_factors


variables = {}
base_name = 'factors_of_'
for i in range(1,24):
    key = f'{base_name}{i}'
    variables[key] = count_factors(i) 


print(variables)
