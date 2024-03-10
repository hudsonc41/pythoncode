sum = 0
for i in range(1000):
    number = i
    if number % 3 == 0:
        sum += number
    elif number % 5 == 0:
        sum += number

print(sum)
