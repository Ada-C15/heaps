from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(log n)
        Space Complexity: ?
    """
    heap = MinHeap()
    for num in list:
        heap.add(num)
    
    heap_list = []
    while heap.store:
        num = heap.remove()
        heap_list.append(num)
    return heap_list