# sorting algorithms

def merge(array, left, pivot, right):
    n1 = pivot - left + 1
    n2 = right - pivot

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = array[left + i]

    for j in range(0, n2):
        R[j] = array[pivot + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


# left index and right index of the sub-array of arr to be sorted
def mergeSort(array, left, right):
    if left < right:
        pivot = left+(right-left)//2

        # Sort first and second halves
        mergeSort(array, left, pivot)
        mergeSort(array, pivot+1, right)
        merge(array, left, pivot, right)


def mergemain(arr):
    n = len(arr)
    print("Given array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")

    print("\n\nMerge Sort")
    mergeSort(arr, 0, n-1)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")
