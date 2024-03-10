total_sum = 0
even_numbers = []
numbers = [1, 2]

while numbers[0] < 4000000 or numbers[1] < 4000000:
    if numbers[1] % 2 == 0:
        total_sum += numbers[1]
    fibbonaci_number = sum(numbers)
    numbers.pop(0)
    numbers.append(fibbonaci_number)
    print(total_sum)

print(numbers)

print(total_sum)
