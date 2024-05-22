import random
import pprint

def count_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:
            count += 1
            if i != n // i:  # Check if the divisor is not the square root of n to avoid counting it twice
                count += 1
    return count


factors = [[] for _ in range(100)]

for i in range(2, 100):
    for j in range(2, int(i/2 + 1)):
        if i % j == 0:
            factors[i].append(j)


prime_numbers = []

for i in range(2, 100):
    prime = (len(factors[i]) == 0)
    if prime == True:
        prime_numbers.append(i)

print(prime_numbers)

#pprint.pprint (factors)

number = random.randrange(2, 100)
while number in prime_numbers:
    number = random.randrange(2, 100)
number_of_factors = len(factors[number])

random_factor = random.choice(factors[number])
print(random_factor)
print(number)