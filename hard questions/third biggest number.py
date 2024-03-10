##def third_biggest_number(numbers):
##    biggest = numbers[0]
##    second = numbers[0]
##    third = numbers[0]
##    for i in range(1, len(numbers)):
##        number = numbers[i]
##        if number > biggest:
##            number = biggest
##        elif number > second:
##            number = second
##        elif number > third:
##            number = third
##    return third
##
##numbers = input('Numbers: ')
##print(f'The third biggest number is {third_biggest_number(numbers)}.')


def third_biggest_number(numbers):
    for number in numbers:
        number = int(number)
    numbers.sort()
    print(numbers)
    return numbers[-3]


numbers = input("Numbers: ").split()
print(f"The third biggest number is {third_biggest_number(numbers)}.")
