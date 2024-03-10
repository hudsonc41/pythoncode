def area_sqaure(side_length):
    area = side_length**2
    return area


def main():
    side = float(input("Side Length of Square: "))
    area = area_sqaure(side)
    print(area)


main()
