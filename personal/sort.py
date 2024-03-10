def merge_sort(array):
    length = len(array)
    middle = length // 2
    first_half = array[:middle]
    latter_half = array[middle:]
    merge_sort(first_half)
    merge_sort(latter_half)
