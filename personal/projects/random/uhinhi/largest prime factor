from math import ceil


def is_prime(num):
    if num in [0, 1]:
        return False
    else:
        for i in range(2, ceil(num ** (1 / 2) + 1)):
            if num % i == 0:
                return False
        return True


num = 600851475143
lpf = None
for i in range(2, ceil(num ** (1 / 2) + 1)):
    if num % i == 0 and is_prime(i) == True:
        lpf = i

print(lpf)
