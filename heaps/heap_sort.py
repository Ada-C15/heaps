from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """

    sortedArray = []
    heap = MinHeap()

    # insert list items into heap
    for item in list:
        heap.add(item, item)
        
    # remove list items from heap
    heapItemValue = heap.remove() 
    while heapItemValue != None:
        sortedArray.append(heapItemValue)
        heapItemValue = heap.remove()

    return sortedArray