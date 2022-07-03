
def selectionsort(arr):
    size = len(arr)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if arr[i] < arr[min_idx]:
                min_idx = i

        # put min at the correct position
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

    return arr


def selectionmain(arr):
    n = len(arr)
    result = selectionsort(arr)

    print("\n\nQuickSort")
    print("Sorted array is")
    for i in range(n):
        print("%d" % result[i], end=" ")
