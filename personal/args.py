def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


print(add(1, 2, 4, 5, 2, 3))


def hello(**kwargs):
    print("hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first_name="John", last_name="Smith")
