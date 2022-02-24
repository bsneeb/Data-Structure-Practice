''' Selection sort:
    Selects smallest element from list and places it in the 
    beginning of the list.
    Complexity:
        Time:
            Best:   O(n^2)
            Avg:    O(n^2)
            Worst:  O(n^2)
        Space:  O(1)
    Applications:
        Small list sorts
        Cost of swapping doesnt matter
'''


def selection_sort(arr):
    '''Select smallest element from list and place it in the beginning of the list'''
    size = len(arr)
    for step in range(size):
        min = step
        for i in range(step+1, size):
            if arr[i] < arr[min]:
                min = i
        arr[step], arr[min] = arr[min], arr[step]
    print(arr)

if __name__ == '__main__':
    array = [-1, 0, 6, 2, 15, 5, 9, 8, 4]
    selection_sort(array)
