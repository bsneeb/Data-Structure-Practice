''' Binary Search
    Finding an elements position in a sorted array. Can be done iterative
    or recursive.
    Complexity:
        Time:
            Best:   O(1)
            Avg:    O(log(n))
            Worst:  O(log(n))
        Space:  O(1)
'''

def bin_search(arr, x, low, high):

    if high >= low:
        mid = low + (high - low) // 2

        # If found at mid, return it
        if arr[mid] == x:
            return f"Found at position: {mid}"
        
        # Search left half
        elif arr[mid] > x:
            return bin_search(arr, x, low, mid-1)
        
        # Search right half
        else:
            return bin_search(arr, x, mid+1, high)
    
    else:
        return f"Not Found"

if __name__ == '__main__':

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 3
    print(bin_search(array, x, 0, len(array) - 1))
        
