from math import ceil


def is_prime(num):
    print("hi")
    if num in [0, 1]:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, ceil(num ** (1 / 2) + 1)):
            if num % i == 0:
                return False
        return True


def prime_factors(num):
    print("hi")
    pf = []

    for i in range(2, num):
        if num % i == 0:
            if is_prime(num % i) == True:
                pf.append(i)
    return pf


def euler_totient(number):
    if is_prime(number) == True:
        return number - 1
    else:
        return


print(prime_factors(55))
