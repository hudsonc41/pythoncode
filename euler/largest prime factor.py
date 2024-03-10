
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

    
number = int(input('Number: '))
prime_numbers = []
prime_factors = []
for i in range(1, number + 1):
    factors = find_factors(i)
    if len(factors) == 2:
        prime_numbers.append(i)
for prime_number in prime_numbers:
    if number % prime_number == 0:
        prime_factors.append(number)

print(prime_factors)
        


                
