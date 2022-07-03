# pretty bad sorting overall

def bubbleascending(arr, n):
    for i in range(n):

        for j in range(0, n-1-i):
            # sort values from least to greatest
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubbledescending(arr, n):
    for i in range(n):

        for j in range(0, n-1-i):
            # sort values from greatest to least
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubblemain(arr):
    n = len(arr)
    array1 = arr.copy()
    array2 = arr.copy()
    result = bubbleascending(array1, n)
    result2 = bubbledescending(array2, n)

    print("\n\nBubble Sort")

    print("Ascending sorted array is")
    print(result)

    print("\n\nDescending sorted array is")
    print(result2)
