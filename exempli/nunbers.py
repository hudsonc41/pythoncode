def count_up(num):
    i = 1
    while i <= num:
        print(i)
        i += 1


def left_triangle(num):
    i = 1
    while i <= num:
        print("*" * i)
        i += 1


def rectangle(num):
    i = 0
    while i < num:
        print("*" * num)
        i += 1


def right_triangle(num):
    i = num - 1
    while i >= 0:
        print(" " * i + "*" * (num - i))
        i -= 1


def triangle(num):
    i = 1
    while i <= num:
        print(
            " " * (num - i) + "*" * ((num * 2 - 1) - (2 * (num - i))) + " " * (num - i)
        )
        i += 1


def diamond(num):
    i = 1
    while i <= num:
        print(
            " " * (num - i) + "*" * ((num * 2 - 1) - (2 * (num - i))) + " " * (num - i)
        )
        i += 1
    i -= 1
    while i > 1:
        print(
            " " * (num - i) + "*" * ((num * 2 - 1) - (2 * (num - i))) + " " * (num - i)
        )
        i -= 1


num = int(input("Number: "))

count_up(num)
print()
left_triangle(num)
print()
rectangle(num)
print()
right_triangle(num)
print()
triangle(num)
print()
diamond(num)
