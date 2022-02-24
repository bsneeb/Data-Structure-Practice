''' Bubble sort: 
    Compare two adjacent elements and swap until they are sorted.
    Complexity:
        Time:
            Best:  O(n)
            Avg:   O(n^2)
            Worst: O(n^2)
        Space: O(1)
    Applications:
        Sort if complexity does not matter
        Short and simple code
'''


def bubble_sort(arr):
    ''' Compare two adjacent elements and swap until sorted '''
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


def improved_bubble_sort(arr):
    ''' Improve bubble sort so it does not swap already sorted elements '''
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            break
    print(arr)


if __name__ == '__main__':

    array = [9, 4, 1, 3, 6, 12, 9, 0, 2]
    bubble_sort(array)
    improved_bubble_sort(array)