def part_1(num):
    while num > 0:
        print("a" * num)
        num -= 1
    print("Finis")


def bob():
    print("bob")


def count_up(num):
    i = 0
    while i < num:
        print(1)
        i += 1
    print("finis")


bob()
num = int(input("number"))
part_1(num)
