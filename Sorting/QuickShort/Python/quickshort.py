import sys


def partition(arr, low, high):
    """ This function takes  last element as pivot, places the pivot element at
    its correct  position in sorted array, and places all smaller (smaller than
    pivot) to left of pivot and all greater elements to right of pivot.

    Attributes:
        :arr:   List of integers.
        :low:   Starting index
        :high:  Ending index
    """

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    """ The main function that implements QuickSort.

    Attributes:
        :arr:   List of integers.
        :low:   Starting index
        :high:  Ending index
    """

    if low < high:

        # pi is partitioning index, arr[p] is now at right place.
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition.
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def main():
    arr = [int(i) for i in sys.argv[1:]]
    n = len(arr)

    quickSort(arr, 0, n-1)

    print(arr)


if __name__ == '__main__':
    main()
