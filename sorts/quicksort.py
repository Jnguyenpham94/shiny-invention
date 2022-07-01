
def quicksort(arr):
    n = len(arr)

    # Base case
    if n < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, n):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    # Sorts the elements to the left of pivot
    left = quicksort(arr[0:current_position])
    # sorts the elements to the right of pivot
    right = quicksort(arr[current_position+1:n])

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr


def quickmain(arr):
    n = len(arr)
    result = quicksort(arr)

    print("\n\nQuickSort")
    print("Sorted array is")
    for i in range(n):
        print("%d" % result[i], end=" ")
