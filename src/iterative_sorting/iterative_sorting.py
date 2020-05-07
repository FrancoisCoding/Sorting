def selection_sort(arr):
    length = range(0, len(arr) - 1)
    for i in length:
        smallest_value = i
        # Compares the current smallest value to values to the right
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_value]:
                smallest_value = j

        # Switches values if the smallest_value is changed
        if smallest_value != i:
            arr[smallest_value], arr[i] = arr[i], arr[smallest_value]

    # Return sorted array
    return arr


def bubble_sort(arr):
    length = len(arr) - 1
    for i in range(length, 0, -1):
        for j in range(i):
            # Compares first value on the left to value after
            if arr[j] > arr[j + 1]:
                # Swaps to values
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return sorted array
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
