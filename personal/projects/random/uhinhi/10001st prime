from math import ceil

primes = []


def is_prime(num):
    if num in [0, 1]:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, ceil(num ** (1 / 2) + 1)):
            if num % i == 0:
                return False
        return True


num = 1
while len(primes) <= 10001:
    primality = is_prime(num)
    if primality == True:
        primes.append(num)
    num += 1

print(primes[0])
print(primes[10000])
