''' Insertion sort:
    Places unsorted element at its correct position each iteration.
    Complexity:
        Time:
            Best:   O(n)
            Avg:    O(n^2)
            Worst:  O(n^2)
        Space: O(1)
    Applications:
        Best when array has small number of elements
        There are few elements to be sorted
'''

def insertion_sort(arr):
    '''Places unsorted elements at its correct position each iteration'''
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    print(arr)
    
if __name__ == '__main__':
    array = [9, 3, 5, 1, 2, 5, 3, 7, 8]
    insertion_sort(array)