import math


def area_triangle(base, height):
    area = 0.5 * base * height
    return area


def area_square(side_length):
    area = side_length**2  # raised to power of 2
    return area


def quadratic_function(a, b, c):
    d = math.sqrt((b**2) - (4 * a * c))
    x = ((b * -1) - d) / (2 * a)
    y = ((b * -1) + d) / (2 * a)
    sol = (round(x, 4), round(y, 4))
    return sol


def determinant(a, b, c):
    d = (b**2) - (4 * a * c)
    if d > 0:
        return "Two solutions"
    elif d == 0:
        return "One solution"
    else:
        return "No solution"


print(quadratic_function(10, 100, 10))
print(determinant(10, 100, 10))

##base = float(input('Base: '))
##height = float(input('Height: '))
##answer = area_triangle(base, height)
##print(f'A triangle with base of {base} and height of {height} has an area of {answer}')
