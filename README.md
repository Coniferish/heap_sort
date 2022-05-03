After reading through tutorials and explanations online about heap sort, I decided to make my own overly-commented version.

### Pros
- Worst case O(nlogn) time
- Partially sorted result if the sort gets interrupted
- In-place (memory)

### Cons
- Relatively slow compared to QuickSort (the constant time is greater)
- "Not stable"
- Not adaptive/doesn't matter if the input is already semi-sorted

**Note** (and this may be obvious to others, but it wasn't immediately to me): <br />
We're only dealing with arrays. We don't actually have to access or create a "heap" 
structure (we're just applying that framework/perspective to an array).
<br />
<br />
<br />
I'm not going to expain how we could logically come to this approach since heaps are 
still new to me, so lets accept that we're using a max (or min) heap. 

### Getting local maximum to the parent node (and working towards a max heap):
- Heapify is called on a single node, but recursively calls itself if the parent node was swapped with a child node 
- It ASSUMES THE CHILDREN ARE ALREADY SORTED (HeapSort starts at the bottom "leaves" and works up to the top "root", and Heapify works its way down as it moves a small-value-parent down to its an appropriate position)
- Arguments to pass in:
    - The array (obvious)
    - The current/parent node
    - The length of the array (needed so we don't try to access children nodes that don't actually exist)

```diff
+ calculate the left and right children
+ check if either child is greater than the parent
+ swap if a child is greater
+ call heapify on the swapped index/check those children
def heapify(arr, parent_i, length):
    left_i = parent_i*2 + 1
    right_i = left_i + 1
    temp_i = parent_i 
+ we want to keep track of the index of the largest value and not the actual 
+ largest value because we need the index to swap values

+ remember that the first condition is checked first   
    if left_i < length and arr[left_i] > arr[temp_i]:
        temp_i = left_i
    if right_i < length and arr[right_i] > arr[temp_i]:
        temp_i = right_i
    if parent_i != temp_i:
        arr[temp_i], arr[parent_i] = arr[parent_i], arr[temp_i]
+ at this point temp_i is pointing to the child node which now contains
+ the value that started at the parent node
        heapify(arr, temp_i, length)
        
    return arr
```

If you call heapify() on an array, it will not necessarily put the max value at the root. 
That would only happen if the max value was already a direct child of the root node. 
If it is not, then the max value is stuck in a lower level of the tree. This is why we have 
to iterate from the bottom leaves up to the root and call heapify() on each parent node.

HeapSort does this job (of making a max/min heap) *and then* moves the root node to the end and "prunes" the tree (the actual length of the 
array doesn't change, but iterating over length of the array acts like it does. This means we 
don't have to use more memory/space). It does mean that the final array will be sorted in the opposite direction the heap was sorted:
a max heap gives an array from least to greatest.

HeapSort loops over the parent nodes and calls Heapify on them (starting at the bottom)<br />
We need to know: <br />
- The length and last node (length-1)
- The last-parent-node: `(arr.length() // 2) - 1` (from here we need to iterate to the root)

```diff
+ max-heapify the array
+ swap the root/max with the last index
+ heapify the array again
+ repeat swapping and heapifying until you get to a length of 1 node 
def heapSort(arr):
    length = len(arr)
    last_parent =  (arr.length() // 2) - 1

+ because the children have to be heaps, we have to start at the last parent node
+ and work our way up to the root, visiting every parent node in order to get
+ the max value to the root.
    for i in range(last_parent, -1, -1): 
        heapify(arr, i, length)
 
+ The max is now at the root, so we can move it to the end of the array 
+ and call heapify on the array again. This time heapify will only need to put
+ the updated value in its correct place and bring the next max value to the root
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
```    
 
One thing to note is that we have to go through this process of moving the max value to the end of the heap and shorten the heap from the rear because shortening it from the front would create a big change in the heap structure. Remember that we're using an array to represent the heap, so shifting the index of every node would be really disruptive.

   (max-heap)            >>>            (NOT A MAX-HEAP)
   
[9, 4, 8, 2, 0, 5, 7] >>>      [9][4, 8, 2, 0, 5, 7]

           9            >>>           4
        4     8                    8    2
      2  0   5  7                0  5   7
