sum_of_squares = 0
for i in range(101):
    square = i ** 2
    sum_of_squares += square

print(sum_of_squares)


summ = 0
for i in range(101):
    summ += i
square_of_sum = summ ** 2
print(summ)
print(square_of_sum)

difference = square_of_sum - square_of_sum
print(difference)
