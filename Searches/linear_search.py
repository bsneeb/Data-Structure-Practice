''' Linear Search
    Sequential searching algorithm that starts from one end and checks
    every element of the list until the element is found. Most simple 
    searching algorithm.
    Complexity:
        Time:   O(n)
        Space:  O(1)
    Applications:
        Best for searches on small arrays
'''

def linear_search(arr, n):

    for i in range(0, len(arr)):
        if arr[i] == n: 
            return f"Found the element {n} at index {i}!"
    return f"Element {n} not found."

if __name__ == '__main__':
    array = [9, 4, 14, 5, 23, 566, 21, 662, 1, 2, 6, 0, 83, 4]
    print(linear_search(array, 16))
    print(linear_search(array, 6))