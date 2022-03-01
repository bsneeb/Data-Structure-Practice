''' Heap Sort
    Popular and efficient. Requires arrays and trees.
    Complexities:
        Time:
            Best:   O(nlog(n))
            Avg:    O(nlog(n))
            Worst:  O(nlog(n))
        Space:  O(1)
'''

def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is largest
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right child is largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If root is not the largest, swap and recursivley heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':

    array = [8, 5, 32, 5, 66, 12, 3, 9, 0, 4, 13]
    heap_sort(array)
    n = len(array)
    for i in range(n):
        print(array[i])

    