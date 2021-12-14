from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    hold_heap = MinHeap()
    for x in list:
        hold_heap.add(x)

    return [hold_heap.remove() for i in range(len(list))]
