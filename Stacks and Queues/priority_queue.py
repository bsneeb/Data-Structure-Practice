''' Implementing a priority queue in python. This is a special
    type of queue that associates a priority value to each element.
    No more FIFO, since it is based on priority value now. This
    Data Structure is based on the Heap, using functions such as
    heapify.
    Applications:
        Dijkstras algorithm
        implementing stack
        load balancing on interrupts in OS
'''


def heapify(arr, n, i):
    ''' Finds the largest amoung root, left and right child '''
    largest = i
    left = 2*i+1
    right = 2*i+2

    # Check if left is largest
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right is largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Swap and continue to heapify if root isnt largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, item):
    size = len(array)
    if size == 0:
        array.append(item)
    else:
        array.append(item)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def deleteNode(array, item):
    size = len(array)
    i = 0
    for i in range(0, size):
        if item == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(item)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


if __name__ == '__main__':

    arr = []

    insert(arr, 1)
    insert(arr, 10)
    insert(arr, 3)
    insert(arr, 45)
    insert(arr, 2)
    insert(arr, 7)
    insert(arr, 8)

    print(f"Max heap array: {str(arr)}")

    deleteNode(arr, 10)

    print(f"Max heap array (after deletion): {str(arr)}")
