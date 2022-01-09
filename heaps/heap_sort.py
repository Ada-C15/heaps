from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    heap = MinHeap()
    sorted_list = []

    for value in list:
        heap.add(value)

    while heap.store:
        sorted_list.append(heap.remove())
    return sorted_list