def longest_rise(stock_data):
    rises = []
    rise = 0
    for i in range(1, len(stock_data)):
        if stock_data[i] > stock_data[i - 1]:
            rise += 1
            if i == len(stock_data) - 1:
                rises.append(rise)
        else:
            rises.append(rise)
            rise = 0
    return rises


stock_data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 2, 4, 5, 2, 6, 3, 5]
length = longest_rise(stock_data)
print(length)
print(f"The longest continuous rise is {max(length)}.")


def longest_rise2(stock_data):
    longest_rise = 0
    rise = 0
    for i in range(1, len(stock_data)):
        if stock_data[i] > stock_data[i - 1]:
            rise += 1
        else:
            rise = 0
        longest_rise = max(longest_rise, rise)
    return longest_rise


print(longest_rise2(stock_data))
