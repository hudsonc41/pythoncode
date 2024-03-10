##number = int(input('Enter a number for the timetables: '))
##for i in range(1, 13):
##    print(f'{number} X {i} = {number * i}')
##
##print()
##print('All time timestables')
##for i in range(1, 13):
##    print()
##    for e in range(1, 13):
##        print(f'{i} X {e} = {i * e}')

import random

i = 0
while i < 3:
    number_1 = random.randint(1, 13)
    number_2 = random.randint(1, 13)
    answer = int(input(f"What is {number_1} * {number_2}? "))
    if answer == (number_1 * number_2):
        print("Correct!")
    else:
        print("Wrong!")
        i += 1
print("Game over.")
exit()
