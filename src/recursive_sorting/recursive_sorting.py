# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    k = 0

    if len(arrA) < 1:
        return arrB

    if len(arrB) < 1:
        return arrA

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            print(arrA[i])
            merged_arr[k] = arrA[i]
            i += 1
            k += 1

        else:
            merged_arr[k] = arrB[j]
            j += 1
            k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr = arrB[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # -1. Create condition to stop recursion when lists contain one element
    if len(arr) > 1:
        # -2. Find middle of list
        mid = len(arr) // 2
        # -3. Split list into two parts
        left_list = arr[:mid]  # This list is from beginning to mid
        right_list = arr[mid:]  # This list is from mid to end
        # -4. Divide lists again using recursion
        merge_sort(left_list)
        merge_sort(right_list)
        # -5. Merge lists
        # Index for left list
        i = 0
        # Index for right list
        j = 0
        # Index for original list
        k = 0
        # -6. Create while loop for the case that lists contain a length of more than 1
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                arr[k] = left_list[i]
                i += 1
                k += 1
            else:
                arr[k] = right_list[j]
                j += 1
                k += 1
        # -7. Check if any elements of lists are skipped
        while i < len(left_list):
            arr[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            arr[k] = right_list[j]
            j += 1
            k += 1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
