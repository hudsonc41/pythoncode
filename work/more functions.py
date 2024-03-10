def area_triangle(base, height):
    area = 0.5 * base * height
    print(area)


base = float(input("Base: "))
height = float(input("Height: "))
answer = area_triangle(base, height)
print(f"A triangle with base of {base} and height of {height} has an area of {answer}")
