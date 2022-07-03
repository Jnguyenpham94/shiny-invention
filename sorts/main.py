import sys
import mergesort
import bubblesort
import quicksort
import selectionsort


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    while True:
        x = input(
            "\n0.exit\n1. Merge Sort\n2. Bubble Sort\n3. Quick Sort\n4.Selection Sort\n")
        if x == 0:
            break
        if x == "1":
            mergesort.mergemain(arr)
        if x == "2":
            bubblesort.bubblemain(arr)
        if x == "3":
            quicksort.quickmain(arr)
        if x == "4":
            selectionsort.selectionmain(arr)
    sys.exit("GOODBYE")
