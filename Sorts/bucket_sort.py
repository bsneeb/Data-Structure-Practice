''' Bucket Sort
    Divides the unsorted array elements into several groups called buckets.
    Each bucket is then sorted by using any suitable sorting algorithm 
    or recursivly applying the same bucket algorithm.
    Complexity:
        Time:
            Best:   O(n+k)
            Avg:    O(n)
            Worst:    O(n^2)
        Space:  O(n+k)
    Applications:
        Input is uninformly distributed over a range
        There are floating point values
'''


def bucket_sort(arr):

    bucket = []

    # Create empty buckets
    for i in range(len(arr)):
        bucket.append([])

    # Insert elements into their respective buckets
    for x in arr:
        bucket_idx = int(10 * x)
        bucket[bucket_idx].append(x)

    # Sort the elements of each bucket
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k  = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    
    return arr

if __name__ == '__main__':

    arr = [.42, .32, .33, .52, .37, .47, .51, .55, .09, .01]

    print(bucket_sort(arr))