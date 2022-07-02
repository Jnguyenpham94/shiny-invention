import mergesort
import bubblesort
import quicksort


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    while True:
        x = input("\n1. Merge Sort\n2. Bubble Sort\n3. Quick Sort\nexit\n")
        if x == "1":
            mergesort.mergemain(arr)
        elif x == "2":
            bubblesort.bubblemain(arr)
        elif x == "3":
            quicksort.quickmain(arr)
        elif x == "exit":
            break
