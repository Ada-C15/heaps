from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    heap = MinHeap()
    for element in list:
        heap.add(element)

    sortedList = []
    while heap.store:
        element = heap.remove()
        sortedList.append(element)

    return sortedList