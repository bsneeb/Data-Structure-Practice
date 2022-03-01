''' Quick sort:
    Divide and conquor, dividing array into subarrays and select 
    pivot element.
    Complexity:
        Time:
            Best:   O(nlog(n))
            Avg:    O(nlog(n))
            Worst:  O(n^2)
        Space:  O(log(n))
'''

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



def quicksort(arr, low, high):

    if low < high:
        pivot = partition(arr, low, high)

        quicksort(arr, low, pivot - 1)

        quicksort(arr, pivot + 1, high)


if __name__ == '__main__':
    array = [9, 3, 5, 1, 5, 6, 3, 8, 1, 0]

    quicksort(array, 0, len(array) - 1)
    print(array)