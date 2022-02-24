''' Marge sort:
    Divide and conquor algorithm
    Complexity:
        Time:
            Best:   O(nlog(n))
            Avg:    O(nlog(n))
            Worst:  O(nlog(n))
        Space:  O(n)
    Applications:
        Inversion count problem
        External sorting
        ECommerce applications
'''

def merge_sort(arr):
    if len(arr) > 1:
        r = len(arr)//2
        l = arr[:r]
        m = arr[r:]

        merge_sort(l)
        merge_sort(m)

        i = j = k = 0

        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = m[j]
                j += 1
            k += 1

        while j < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(m):
            arr[k] = m[j]
            j += 1
            k += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end="")

if __name__ == '__main__':
    array = [10, 3, 5, 2, 4, 6, 7, 4, 1, 0]
    merge_sort(array)
    print(array)