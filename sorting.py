def choose_idx(l, r):
    return int((l + r - 1) / 2)


def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp


def divide_table(arr, l, r):
    idx = choose_idx(l, r)
    val = arr[idx]
    swap(arr, idx, r)

    actual_position = l
    for index in range(l, r):
        if arr[index] > val:
            swap(arr, index, actual_position)
            actual_position = actual_position + 1

    swap(arr, actual_position, r)
    return actual_position


def quick_sort(arr, l, r):
    if l < r:
        i = divide_table(arr, l, r)
        quick_sort(arr, l, i - 1)
        quick_sort(arr, i + 1, r)


def my_sort(array):
    quick_sort(array, 0, len(array) - 1)
    return array
