''' Shell Sort
    Shell sort is a generalized version of insertion sort. It first
    sorts elements that are far apart from each other, then continues 
    to reduce the interval between the elements to be sorted.
    Complexities:
        Time:
            Best:   O(nlog(n))
            Avg:    O(nlog(n))
            Worst:  O(n^2)
        Space:  O(1)
    Applications:
        Does not perform well when close elements are far apart.
'''

def shell_sort(arr, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i 
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2

if __name__ == '__main__':

    array = [8, 4, 2, 6, 1, 7, 1, 9, 0]
    size = len(array)
    shell_sort(array, size)
    print(array)

