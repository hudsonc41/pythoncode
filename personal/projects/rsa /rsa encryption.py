import string
import random


def is_prime(number):
    for i in range(number):
        if number % i == 0:
            return False
    return True


def euler_totient(number):
    if is_prime(number) == True:
        return number - 1


lower_chars = [char for char in string.ascii_letters if char.islower()]
conversion = {}
num = 0
for char in lower_chars:
    conversion[char] = str(num)
    num += 1
print(conversion)
msg = input("Word to encrypt: ")
n = "25" * len(msg)
