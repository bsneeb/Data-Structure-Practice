''' Radix Sort
    Sorts the elements by first grouping the individual digits of the 
    same place value. Then, sort the elements according to their increasing/
    decreasing order.
    Complexity:
        Time:
            Best:   O(n+k)
            Avg:   O(n+k)
            Worst:   O(n+k)
        Space:  O(max)
    Applications:
        Places where there are numbers in large ranges
'''



def counting_sort(arr, place):

    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        idx = arr[i] // place
        count[idx % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        idx = arr[i] // place
        output[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]
        
    return arr


def radix_sort(arr):
    max_ele = max(arr)
    place = 1

    # Apply counting sort to sort elements absed on place value
    while max_ele // place > 0:
        counting_sort(arr, place)
        place *= 10

    return arr

if __name__ == '__main__':

    array = [121, 432, 564, 23, 1, 45, 788]

    print(radix_sort(array))