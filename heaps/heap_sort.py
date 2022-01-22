from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    heap = MinHeap()
    for elem in list:
        heap.add(elem)

    hold = []
    while heap.store:
        elem = heap.remove()
        hold.append(elem)

    return hold