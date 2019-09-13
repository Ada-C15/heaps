# Heaps Practice

## Learning Goals

By the end of this lesson you should be able to:

- Implement a heap using an array as an internal data structure
- Use a heap to sort an array
- Correctly identify the space and time complexity of heap and heapsort methods

## Description

In this exercise you will implement a Heap using an array as an internal data structure.  You will also use that heap to write a sorting method.

## MinHeap Class

In this exercise you will implement a MinHeap.  It is recommended that you use an array as the internal data structure of the heap.  We have provided you a HeapNode class to store elements of the Heap.  The Heap will maintain the elements in order using the `key` field to sort by.  That way you could have any type of object and as long as the key is comparable, you can use it to maintain order.

The methods you will need to write are:

- `add(key, value)` - This method takes a key and a value constructs a HeapNode and adds it to the heap.
  - There is a private `heap_up` method.  You may want to implement to do this method to do the add operation.
- `remove()` - This method removes and returns the smallest keyed value from the heap.
  - There is a private `heap_down` method you may want to implement to perform the remove method.
- `empty?` - This method returns true if the heap is empty and false if it's not.

## HeapSort

The last method to write is `heapsort(list)` which takes an array and uses a `Heap` instance to sort the array.  We have discussed this method before.  It should look somewhat like insertion sort.  

Make certain you also document the expected runtime of each method.  

**Challenge** If you can, do this method in O(1) space complexity.

