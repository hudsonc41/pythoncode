##class Dog:
####    def __init__(self, breed, age, weight, colour):
####        self.breed = breed
####        self.age = age
####        self.weight = weight
####        self.colour = colour
##        
##
##    def bark(self):
##        print(str(f'{self} dog barks.'))
##    def eat(self):
##        print(str(f'{self} dog is eating.'))
##
##Doug = Dog()
##print(Doug.bark())

def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


print(add(1, 3, 6, 2, 3))

def fibonacci(stop):
    numbers = []
    number = 0
    numbers.append(number)
    for i in range(0, stop):
        if i == 0:
            number = number + 1
            numbers.append(number)
        else:
            number = number + numbers[i - 1]
            numbers.append(number)
    return numbers
        
    
limit = int(input('Numbers : '))
numbers = fibonacci(limit)
print(numbers)
for number in numbers:
    print(number)
    number = str(number)
print('Numbers: ' + ','.join([str(x) for x in numbers]))
    
    



    

        
            

