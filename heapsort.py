def heapify(arr, parent_i, length):
    left_i = parent_i*2 + 1
    right_i = left_i + 1
    largest_i = parent_i
    
    if left_i < length and arr[left_i] > largest_i:
        largest_i = left_i
    if right_i < length and arr[right_i] > largest_i:
        largest_i = right_i
    if parent_i != largest_i:
        arr[largest_i], arr[parent_i] = arr[parent_i], arr[largest_i]
        heapify(arr, largest_i, length) 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # Swap and "pop" elements off with each iteration
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
 
 
# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
