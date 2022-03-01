''' Counting sort:
    Sorts the elements of an array by counting the number of occurences of each
    unique element in the array. The count is stored in an auxillary array and
    the sorting is done by mapping the count as an index of the aux array.
    Complexity:
        Time:
            Best:   O(n+k)
            Avg:    O(n+k)
            worst:  O(n+k)
        Space:  O(max)
    Applications:
        There are small ints with multiple counts
        Linear complexity is needed
'''


def counting_sort(arr):

    size = len(arr)
    output = [0] * size

    count = [0] * 20

    for i in range(1, size):
        count[arr[i]] += 1

    for i in range(1, 20):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

    print(arr)


if __name__ == '__main__':

    array = [1, 5, 3, 9, 3, 1, 4, 8, 11, 9]

    counting_sort(array)